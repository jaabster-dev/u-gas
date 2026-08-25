import pathlib
import tempfile
import unittest

import sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_u_gas import check_project


class ProjectCheckTests(unittest.TestCase):
    def write_pica(self, root, names):
        for name in names:
            (root / name).write_text("# Existing project control\n", encoding="utf-8")

    def test_all_pica_present_and_anchor(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self.write_pica(root, ("AGENTS.md", "CURRENT_STATE.md", "PROGRESS.md", "IDEAS.md"))
            (root / "AGENTS.md").write_text("This project uses U-GAS\nhttps://github.com/jaabster-dev/u-gas\n", encoding="utf-8")
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
            self.assertIn("AGENTS.md is not readable", check_project(root))
            (root / "AGENTS.md").write_text("This project uses U-GAS\n", encoding="utf-8")
            self.assertIn("U-GAS project AGENTS.md has no canonical upstream anchor", check_project(root))

    def test_checker_does_not_overwrite_substantive_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            original = "# Substantive state\nACTIVE: real work\n"
            (root / "AGENTS.md").write_text("local rules\n", encoding="utf-8")
            (root / "CURRENT_STATE.md").write_text(original, encoding="utf-8")
            before = (root / "CURRENT_STATE.md").read_text(encoding="utf-8")
            check_project(root)
            self.assertEqual((root / "CURRENT_STATE.md").read_text(encoding="utf-8"), before)


if __name__ == "__main__":
    unittest.main()
