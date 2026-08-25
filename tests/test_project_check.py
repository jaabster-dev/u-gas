import pathlib
import tempfile
import unittest

import sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_u_gas import check_project
from pica_contract import CANONICAL_UPSTREAM, load_templates


class ProjectCheckTests(unittest.TestCase):
    def write_pica(self, root, names, current_state=None):
        for name in names:
            (root / name).write_text("# Existing project control\n", encoding="utf-8")
        if current_state is not None:
            (root / "CURRENT_STATE.md").write_text(current_state, encoding="utf-8")

    def valid_agents(self):
        return f"Local project rules\n{CANONICAL_UPSTREAM}\n"

    def valid_resume(self):
        return """# Current State

## ACTIVE
Testing the project.

## NEXT
Inspect the next safe action.

## WAITING/PAUSED
Nothing waiting.

## BLOCKERS/BOUNDARIES
None known.
"""

    def valid_pica(self, root, current_state=None):
        self.write_pica(root, ("AGENTS.md", "CURRENT_STATE.md", "PROGRESS.md", "IDEAS.md"), current_state or self.valid_resume())
        (root / "AGENTS.md").write_text(self.valid_agents(), encoding="utf-8")

    def test_all_pica_present_and_anchor(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.valid_pica(root)
            self.assertEqual(check_project(root), [])

    def test_truthful_minimal_current_state_placeholder_passes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.valid_pica(root, load_templates()["CURRENT_STATE.md"])
            self.assertEqual(check_project(root), [])

    def test_missing_control_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.write_pica(root, ("AGENTS.md", "CURRENT_STATE.md", "IDEAS.md"))
            self.assertIn("missing PICA: PROGRESS.md", check_project(root))

    def test_missing_agents_and_anchor_are_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.write_pica(root, ("CURRENT_STATE.md", "PROGRESS.md", "IDEAS.md"))
            self.assertIn("missing PICA: AGENTS.md", check_project(root))
            (root / "AGENTS.md").write_text("Local project rules only\n", encoding="utf-8")
            self.assertIn("AGENTS.md has no canonical U-GAS upstream anchor", check_project(root))

    def test_anchor_is_required_without_magic_u_gas_phrase(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.write_pica(root, ("AGENTS.md", "CURRENT_STATE.md", "PROGRESS.md", "IDEAS.md"), self.valid_resume())
            (root / "AGENTS.md").write_text("Local project rules without upstream pointer\n", encoding="utf-8")
            self.assertIn("AGENTS.md has no canonical U-GAS upstream anchor", check_project(root))

    def test_empty_pica_control_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.valid_pica(root)
            (root / "PROGRESS.md").write_text("", encoding="utf-8")
            self.assertIn("PROGRESS.md is empty", check_project(root))

    def test_arbitrary_current_state_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.valid_pica(root, "# A random note\nNo resume contract here.\n")
            self.assertIn("CURRENT_STATE.md lacks the canonical minimal placeholder or resume responsibilities", check_project(root))

    def test_checker_does_not_overwrite_substantive_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            original = "# Substantive state\nACTIVE: real work\n"
            (root / "AGENTS.md").write_text("local rules\n", encoding="utf-8")
            (root / "CURRENT_STATE.md").write_text(original, encoding="utf-8")
            before = (root / "CURRENT_STATE.md").read_text(encoding="utf-8")
            check_project(root)
            self.assertEqual((root / "CURRENT_STATE.md").read_text(encoding="utf-8"), before)

    def test_checker_is_read_only_for_a_valid_project(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.valid_pica(root)
            before = {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}
            self.assertEqual(check_project(root), [])
            after = {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}
            self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
