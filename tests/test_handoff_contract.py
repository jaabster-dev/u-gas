import pathlib
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

    def test_branch_resolution_rule_is_valid(self):
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_sample(directory)
            self.assertEqual(check_handoff.validate_file(path), [])

    def test_invalid_branch_shape_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_sample(directory)
            path.write_text(SAMPLE.replace("target_branch: main", "target_branch: ../main"), encoding="utf-8")
            self.assertTrue(any("target_branch" in error for error in check_handoff.validate_file(path)))

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
