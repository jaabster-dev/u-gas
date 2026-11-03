#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, io, pathlib, subprocess, sys, tempfile, unittest
from contextlib import redirect_stdout
from unittest.mock import patch

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("repository_health", ROOT / "scripts" / "check_repository_health.py")
health = importlib.util.module_from_spec(spec); assert spec.loader is not None
sys.modules["repository_health"] = health; spec.loader.exec_module(health)

def git(repo, *args):
    subprocess.run(["git","-C",str(repo),*args], check=True, capture_output=True, text=True)

class RepositoryHealthTests(unittest.TestCase):
    def repo(self):
        td=tempfile.TemporaryDirectory(); p=pathlib.Path(td.name)
        git(p,"init","-b","main"); git(p,"config","user.email","test@example.com"); git(p,"config","user.name","Test")
        (p/"x").write_text("a"); git(p,"add","x"); git(p,"commit","-m","base")
        return td,p

    def test_authority_only_is_green(self):
        td,p=self.repo(); self.addCleanup(td.cleanup)
        self.assertEqual(health.evaluate(p,"main").status,"GREEN")

    def test_authority_ahead_of_release_is_green(self):
        td,p=self.repo(); self.addCleanup(td.cleanup)
        git(p,"branch","release"); (p/"x").write_text("b"); git(p,"commit","-am","work")
        r=health.evaluate(p,"main","release")
        self.assertEqual((r.status,r.authority_ahead,r.release_ahead),("GREEN",1,0))

    def test_release_unique_commit_is_red(self):
        td,p=self.repo(); self.addCleanup(td.cleanup)
        git(p,"branch","release"); git(p,"checkout","release"); (p/"y").write_text("release"); git(p,"add","y"); git(p,"commit","-m","release unique"); git(p,"checkout","main")
        r=health.evaluate(p,"main","release")
        self.assertEqual(r.status,"RED"); self.assertEqual(r.release_ahead,1)

    def test_missing_ref_is_visible_error(self):
        td,p=self.repo(); self.addCleanup(td.cleanup)
        self.assertEqual(health.evaluate(p,"missing").status,"ERROR")


class FakeActionsClient:
    def __init__(self, runs, head="a" * 40, moved_head=None, error=None):
        self.runs = runs
        self.head = head
        self.moved_head = moved_head
        self.error = error
        self.calls = []
        self.branch_reads = 0

    def get(self, path):
        self.calls.append(path)
        if "/branches/" in path:
            self.branch_reads += 1
            return {"commit": {"sha": self.moved_head if self.branch_reads > 1 and self.moved_head else self.head}}
        if "/actions/runs?" in path:
            if self.error:
                raise health.GitHubReadError(self.error)
            return {"workflow_runs": self.runs}
        raise AssertionError(f"unexpected API endpoint: {path}")


class ActionsHealthTests(unittest.TestCase):
    def row(self, run_id, name="checks", head="a" * 40, status="completed", conclusion="success"):
        return {
            "id": run_id, "run_attempt": 1, "name": name, "head_sha": head,
            "status": status, "conclusion": conclusion,
            "created_at": f"2026-11-03T20:{run_id:02d}:00Z",
            "html_url": f"https://github.com/example/project/actions/runs/{run_id}",
        }

    def test_exact_head_ignores_prior_failed_revision(self):
        fake = FakeActionsClient([self.row(2), self.row(1, head="b" * 40, conclusion="failure")])
        result = health.inspect_actions("example/project", "main", fake)
        self.assertEqual((result.status, result.sha), ("PASS", "a" * 40))
        self.assertEqual(len(result.runs), 1)
        self.assertEqual(fake.branch_reads, 2)
        self.assertTrue(all("head_sha=" + "a" * 40 in x for x in fake.calls if "/actions/runs?" in x))

    def test_newer_success_supersedes_same_head_failure(self):
        fake = FakeActionsClient([self.row(3, conclusion="success"), self.row(2, conclusion="failure")])
        result = health.inspect_actions("example/project", "main", fake)
        self.assertEqual(result.status, "PASS")
        self.assertEqual(result.runs[0]["same_sha_failed_runs"], 1)

    def test_repeated_failures_group_by_workflow(self):
        fake = FakeActionsClient([
            self.row(3, conclusion="failure"), self.row(2, conclusion="failure"),
            self.row(1, name="lint", conclusion="success"),
        ])
        result = health.inspect_actions("example/project", "main", fake)
        self.assertEqual(result.status, "FAIL")
        self.assertEqual(len(result.runs), 2)
        self.assertEqual(next(r for r in result.runs if r["workflow"] == "checks")["same_sha_failed_runs"], 2)
        self.assertIn("failed current-SHA runs: 2", health.render_actions(result))

    def test_pending_and_not_run_never_pass(self):
        pending = self.row(1, status="in_progress", conclusion=None)
        self.assertEqual(health.inspect_actions("example/project", "main", FakeActionsClient([pending])).status, "PENDING")
        empty = health.inspect_actions("example/project", "main", FakeActionsClient([]))
        self.assertEqual(empty.status, "NOT_RUN")
        self.assertIn("trigger eligibility", " ".join(empty.notes))

    def test_cancelled_workflow_is_partial_not_success(self):
        result = health.inspect_actions("example/project", "main",
                                        FakeActionsClient([self.row(1, conclusion="cancelled")]))
        self.assertEqual(result.status, "PARTIAL")

    def test_actions_api_denial_preserves_branch_sha_and_unknown(self):
        result = health.inspect_actions("example/project", "main",
                                        FakeActionsClient([], error="GitHub API HTTP 403"))
        self.assertEqual((result.status, result.sha), ("UNKNOWN", "a" * 40))
        self.assertIn("Actions:read", " ".join(result.notes))

    def test_moving_branch_invalidates_snapshot(self):
        result = health.inspect_actions("example/project", "main",
                                        FakeActionsClient([self.row(1)], moved_head="b" * 40))
        self.assertEqual(result.status, "UNKNOWN")
        self.assertIn("changed during", " ".join(result.notes))

    def test_missing_or_bad_run_metadata_is_unknown(self):
        bad = self.row(1)
        bad.pop("run_attempt")
        result = health.inspect_actions("example/project", "main", FakeActionsClient([bad]))
        self.assertEqual(result.status, "UNKNOWN")
        self.assertIn("Malformed", " ".join(result.notes))

    def test_invalid_identity_fails_closed_without_api_call(self):
        fake = FakeActionsClient([])
        result = health.inspect_actions("../../other", "main", fake)
        self.assertEqual(result.status, "UNKNOWN")
        self.assertEqual(fake.calls, [])

    def test_default_local_only_mode_never_constructs_api_client(self):
        with tempfile.TemporaryDirectory() as directory:
            p = pathlib.Path(directory)
            git(p, "init", "-b", "main")
            git(p, "config", "user.email", "test@example.com")
            git(p, "config", "user.name", "Test")
            (p / "x").write_text("local", encoding="utf-8")
            git(p, "add", "x")
            git(p, "commit", "-m", "local")
            output = io.StringIO()
            with patch.object(health, "ActionsClient", side_effect=AssertionError("network not opted in")):
                with redirect_stdout(output):
                    code = health.main(["--repo", str(p), "--authority-branch", "main"])
            self.assertEqual(code, 0)
            self.assertIn("REPOSITORY HEALTH: GREEN", output.getvalue())
            self.assertNotIn("ACTIONS HEALTH:", output.getvalue())

    def test_optional_actions_cli_uses_explicit_repository(self):
        with tempfile.TemporaryDirectory() as directory:
            p = pathlib.Path(directory)
            git(p, "init", "-b", "main")
            git(p, "config", "user.email", "test@example.com")
            git(p, "config", "user.name", "Test")
            (p / "x").write_text("local", encoding="utf-8")
            git(p, "add", "x")
            git(p, "commit", "-m", "local")
            output = io.StringIO()
            with patch.object(health, "ActionsClient", return_value=FakeActionsClient([self.row(1)])):
                with redirect_stdout(output):
                    code = health.main(["--repo", str(p), "--authority-branch", "main",
                                        "--actions", "--github-repository", "example/project"])
            self.assertEqual(code, 0)
            self.assertIn("ACTIONS HEALTH: PASS", output.getvalue())
            self.assertIn("repository: example/project", output.getvalue())


if __name__ == "__main__":
    unittest.main()
