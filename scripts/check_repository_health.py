#!/usr/bin/env python3
"""Read-only local Git branch-health preflight for a U-GAS project."""
from __future__ import annotations
import argparse, json, os, re, subprocess, urllib.error, urllib.parse, urllib.request
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Result:
    status: str
    authority_branch: str
    release_branch: str | None
    authority_ahead: int | None
    release_ahead: int | None
    note: str

def git(repo: Path, *args: str) -> str:
    run = subprocess.run(["git", "-C", str(repo), *args], text=True, capture_output=True)
    if run.returncode:
        raise RuntimeError((run.stderr or run.stdout).strip() or "git command failed")
    return run.stdout.strip()

def evaluate(repo: Path, authority_branch: str, release_branch: str | None = None) -> Result:
    try:
        git(repo, "rev-parse", "--git-dir")
        git(repo, "rev-parse", "--verify", authority_branch)
        if not release_branch or release_branch == authority_branch:
            return Result("GREEN", authority_branch, release_branch, 0 if release_branch else None, 0 if release_branch else None, "authority branch resolved")
        git(repo, "rev-parse", "--verify", release_branch)
        counts = git(repo, "rev-list", "--left-right", "--count", f"{release_branch}...{authority_branch}").split()
        if len(counts) != 2:
            raise RuntimeError("branch comparison returned incomplete counts")
        release_ahead, authority_ahead = map(int, counts)
        if release_ahead:
            return Result("RED", authority_branch, release_branch, authority_ahead, release_ahead, "release branch contains commits outside the authority branch")
        return Result("GREEN", authority_branch, release_branch, authority_ahead, release_ahead, "release branch is contained in authority branch")
    except (RuntimeError, ValueError) as exc:
        return Result("ERROR", authority_branch, release_branch, None, None, str(exc))


@dataclass
class ActionsResult:
    repository: str
    branch: str
    sha: str | None
    status: str
    runs: list[dict]
    notes: list[str]


class GitHubReadError(RuntimeError):
    """A read-only API failure; never an instruction to change permissions or retry indefinitely."""


class ActionsClient:
    """Optional GitHub REST reader. Never used by the default local-only preflight."""

    def __init__(self, token: str | None = None):
        self.token = token

    def get(self, path: str) -> dict:
        headers = {"Accept": "application/vnd.github+json", "User-Agent": "u-gas-repository-health"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        request = urllib.request.Request(f"https://api.github.com{path}", headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                payload = json.load(response)
        except urllib.error.HTTPError as exc:
            raise GitHubReadError(f"GitHub API HTTP {exc.code}") from exc
        except (urllib.error.URLError, TimeoutError, UnicodeError, json.JSONDecodeError) as exc:
            raise GitHubReadError(f"GitHub API response unavailable: {type(exc).__name__}") from exc
        if not isinstance(payload, dict):
            raise GitHubReadError("GitHub API returned a non-object payload")
        return payload


def inspect_actions(repository: str, branch: str, client: ActionsClient) -> ActionsResult:
    """Summarize only workflows observed at an exact remote branch HEAD; no mutations."""
    sha: str | None = None
    try:
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
            raise GitHubReadError("invalid explicit GitHub repository identity")
        if not branch or not isinstance(branch, str):
            raise GitHubReadError("authoritative branch was not established")
        prefix = f"/repos/{urllib.parse.quote(repository, safe='/')}"
        branch_path = f"{prefix}/branches/{urllib.parse.quote(branch, safe='')}"
        first = client.get(branch_path)
        commit = first.get("commit")
        sha = commit.get("sha") if isinstance(commit, dict) else None
        if not isinstance(sha, str) or not re.fullmatch(r"[0-9a-f]{40}", sha):
            raise GitHubReadError("remote authoritative branch HEAD unavailable")
        payload = client.get(f"{prefix}/actions/runs?head_sha={sha}&per_page=100")
        raw = payload.get("workflow_runs")
        if not isinstance(raw, list):
            raise GitHubReadError("Actions response is missing workflow_runs")
        latest: dict[str, tuple[tuple[str, int, int], dict]] = {}
        failure_counts: dict[str, int] = {}
        incomplete = False
        for run in raw:
            if not isinstance(run, dict) or run.get("head_sha") != sha:
                continue
            name, status, conclusion = run.get("name"), run.get("status"), run.get("conclusion")
            attempt, run_id, created = run.get("run_attempt"), run.get("id"), run.get("created_at")
            if (not isinstance(name, str) or not name or
                    status not in {"queued", "in_progress", "pending", "waiting", "requested", "completed"} or
                    type(run_id) is not int or type(attempt) is not int or
                    not isinstance(created, str) or not created or
                    (status == "completed" and conclusion is None)):
                incomplete = True
                continue
            if conclusion in {"failure", "timed_out", "action_required"}:
                failure_counts[name] = failure_counts.get(name, 0) + 1
            rank = (created, attempt, run_id)
            if name not in latest or rank > latest[name][0]:
                latest[name] = (rank, {
                    "workflow": name, "status": status, "conclusion": conclusion,
                    "url": run.get("html_url") if isinstance(run.get("html_url"), str) else None,
                })
        # A moving branch invalidates the snapshot, even if the first response was green.
        last = client.get(branch_path)
        last_commit = last.get("commit")
        if not isinstance(last_commit, dict) or last_commit.get("sha") != sha:
            raise GitHubReadError("remote branch HEAD changed during Actions inspection")
        rows = []
        for name in sorted(latest):
            row = dict(latest[name][1])
            row["same_sha_failed_runs"] = failure_counts.get(name, 0)
            rows.append(row)
        if incomplete:
            result = "UNKNOWN"
        elif not rows:
            result = "NOT_RUN"
        elif any(row["conclusion"] in {"failure", "timed_out", "action_required"} for row in rows):
            result = "FAIL"
        elif any(row["status"] != "completed" for row in rows):
            result = "PENDING"
        elif any(row["conclusion"] != "success" for row in rows):
            result = "PARTIAL"
        else:
            result = "PASS"
        notes = ["Only observed workflows on the exact remote HEAD were checked; missing trigger coverage remains unverified."]
        if incomplete:
            notes.append("Malformed or incomplete current-HEAD run metadata; cannot claim PASS.")
        if not rows:
            notes.append("No Actions runs found; trigger eligibility and required checks were not determined.")
        if len(raw) == 100:
            notes.append("First API page reached 100 runs; older workflow history may be incomplete.")
        return ActionsResult(repository, branch, sha, result, rows, notes)
    except (GitHubReadError, TypeError, ValueError, KeyError) as exc:
        notes = [f"GitHub Actions read not verified: {exc}"]
        if "HTTP 403" in str(exc):
            notes.append("Check repository access and Actions:read permission; the specific authorization cause is UNKNOWN.")
        return ActionsResult(repository, branch, sha, "UNKNOWN", [], notes)


def render_actions(result: ActionsResult) -> str:
    lines = [f"ACTIONS HEALTH: {result.status}", f"repository: {result.repository}",
             f"remote authority: {result.branch} / {result.sha or 'UNKNOWN'}"]
    for row in result.runs:
        lines.append(f"- {row['workflow']}: {row['conclusion'] or row['status']} ({row['url'] or 'no URL'})"
                     f"; failed current-SHA runs: {row['same_sha_failed_runs']}")
    lines.extend(f"note: {note}" for note in result.notes)
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--authority-branch", required=True)
    parser.add_argument("--release-branch")
    parser.add_argument("--actions", action="store_true", help="Opt in to read-only GitHub Actions current-HEAD inspection")
    parser.add_argument("--github-repository", help="Explicit owner/repo identity, required with --actions")
    args = parser.parse_args(argv)
    if args.actions != bool(args.github_repository):
        parser.error("--actions requires --github-repository owner/repo (and vice versa)")
    result = evaluate(args.repo, args.authority_branch, args.release_branch)
    print(f"REPOSITORY HEALTH: {result.status}")
    print(f"authority: {result.authority_branch}")
    print(f"release: {result.release_branch or '-'}")
    if result.authority_ahead is not None:
        print(f"authority-ahead: {result.authority_ahead}")
        print(f"release-ahead: {result.release_ahead}")
    print(f"note: {result.note}")
    actions = None
    if args.actions:
        actions = inspect_actions(args.github_repository, args.authority_branch, ActionsClient(os.getenv("GITHUB_TOKEN")))
        print(render_actions(actions))
    return 0 if result.status == "GREEN" and (actions is None or actions.status not in {"FAIL", "UNKNOWN"}) else 1

if __name__ == "__main__":
    raise SystemExit(main())
