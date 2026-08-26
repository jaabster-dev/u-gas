import pathlib
import contextlib
import io
import os
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import check_handoff

SAMPLE = """# Test handoff

- id: sample-handoff-20260826
- status: PENDING
- created: 2026-08-26
- target_repository: other/repository
- target_branch: main

## Objective
Test objective.

## Execution instructions
Test instructions.

## Constraints
Test constraints.

## Required verification
Test verification.

## Completion / consumption rule
Test consumption.
"""


class HandoffContractTests(unittest.TestCase):
    def write_sample(self, directory, name="sample-handoff-20260826.md"):
        path = pathlib.Path(directory) / name
        path.write_text(SAMPLE, encoding="utf-8")
        return path

    def test_empty_pending_surface_is_valid(self):
        self.assertEqual(check_handoff.validate_directory(ROOT / "handoffs/pending"), [])

    def test_pending_sample_is_valid(self):
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_sample(directory)
            self.assertEqual(check_handoff.validate_file(path), [])

    def test_generic_target_without_assertion_is_valid(self):
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_sample(directory)
            self.assertEqual(check_handoff.validate_file(path), [])

    def test_target_assertion_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_sample(directory)
            errors = check_handoff.validate_file(path, "different/repository")
            self.assertTrue(any("must be exactly different/repository" in error for error in errors))

    def test_exact_pending_handoff_is_launcher_ready(self):
        with tempfile.TemporaryDirectory() as directory:
            pending = pathlib.Path(directory)
            self.write_sample(pending)
            self.assertEqual(
                check_handoff.validate_exact_handoff(pending, "sample-handoff-20260826", "other/repository"),
                [],
            )

    def test_exact_cli_emits_launcher_ready(self):
        with tempfile.TemporaryDirectory() as directory:
            pending = pathlib.Path(directory) / "handoffs" / "pending"
            pending.mkdir(parents=True)
            self.write_sample(pending)
            output = io.StringIO()
            old_cwd = pathlib.Path.cwd()
            try:
                os.chdir(directory)
                with contextlib.redirect_stdout(output):
                    result = check_handoff.main([
                        "--handoff-id", "sample-handoff-20260826",
                        "--target", "other/repository",
                    ])
            finally:
                os.chdir(old_cwd)
        self.assertEqual(result, 0)
        self.assertIn("HANDOFF_READY: sample-handoff-20260826 -> other/repository", output.getvalue())

    def test_exact_pending_handoff_missing_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            errors = check_handoff.validate_exact_handoff(
                pathlib.Path(directory), "missing-handoff-20260826", "other/repository"
            )
        self.assertTrue(any("does not exist" in error for error in errors))

    def test_exact_pending_handoff_wrong_target_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            pending = pathlib.Path(directory)
            self.write_sample(pending)
            errors = check_handoff.validate_exact_handoff(pending, "sample-handoff-20260826", "wrong/repository")
        self.assertTrue(any("must be exactly wrong/repository" in error for error in errors))

    def test_branch_resolution_rule_is_valid(self):
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_sample(directory)
            self.assertEqual(check_handoff.validate_file(path), [])

    def test_invalid_branch_shape_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_sample(directory)
            path.write_text(SAMPLE.replace("target_branch: main", "target_branch: ../main"), encoding="utf-8")
            self.assertTrue(any("target_branch" in error for error in check_handoff.validate_file(path)))

    def test_exact_invalid_branch_fails_launcher_readiness(self):
        with tempfile.TemporaryDirectory() as directory:
            pending = pathlib.Path(directory)
            path = self.write_sample(pending)
            path.write_text(SAMPLE.replace("target_branch: main", "target_branch: ../main"), encoding="utf-8")
            errors = check_handoff.validate_exact_handoff(pending, path.stem, "other/repository")
        self.assertTrue(any("target_branch" in error for error in errors))

    def test_exact_missing_execution_instructions_fails_launcher_readiness(self):
        with tempfile.TemporaryDirectory() as directory:
            pending = pathlib.Path(directory)
            path = self.write_sample(pending)
            path.write_text(SAMPLE.replace("Test instructions.", ""), encoding="utf-8")
            errors = check_handoff.validate_exact_handoff(pending, path.stem, "other/repository")
        self.assertTrue(any("Execution instructions" in error for error in errors))

    def test_exact_missing_constraints_fails_launcher_readiness(self):
        with tempfile.TemporaryDirectory() as directory:
            pending = pathlib.Path(directory)
            path = self.write_sample(pending)
            path.write_text(SAMPLE.replace("Test constraints.", ""), encoding="utf-8")
            errors = check_handoff.validate_exact_handoff(pending, path.stem, "other/repository")
        self.assertTrue(any("Constraints" in error for error in errors))

    def test_exact_consumed_status_fails_launcher_readiness(self):
        with tempfile.TemporaryDirectory() as directory:
            pending = pathlib.Path(directory)
            path = self.write_sample(pending)
            path.write_text(SAMPLE.replace("status: PENDING", "status: CONSUMED"), encoding="utf-8")
            errors = check_handoff.validate_exact_handoff(pending, path.stem, "other/repository")
        self.assertTrue(any("status must be exactly PENDING" in error for error in errors))

    def test_consumed_status_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_sample(directory)
            path.write_text(SAMPLE.replace("status: PENDING", "status: CONSUMED"), encoding="utf-8")
            self.assertTrue(any("status must be exactly PENDING" in error for error in check_handoff.validate_file(path)))

    def test_duplicate_id_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            self.write_sample(directory)
            self.write_sample(directory, "copy.md")
            errors = check_handoff.validate_directory(pathlib.Path(directory))
            self.assertTrue(any("duplicate active handoff id" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
