import pathlib
import re
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_u_gas import AI_FILES, SKILL_FILES, check_distribution


class CoreContractTests(unittest.TestCase):
    def test_distribution_self_check(self):
        self.assertEqual(check_distribution(ROOT), [])

    def test_required_ai_and_skills_exist(self):
        for relative in AI_FILES + SKILL_FILES:
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_skill_inventory_matches_files(self):
        inventory = (ROOT / "skills/README.md").read_text(encoding="utf-8")
        for relative in SKILL_FILES:
            name = pathlib.Path(relative).parent.name
            self.assertIn(f"`{name}`", inventory)

    def test_readme_and_anchor_contract(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("EXPERIMENTAL", readme)
        self.assertIn("NO INDEPENDENT USER VALIDATION YET", readme)
        self.assertIn("PICA SELF-CHECK", readme)
        self.assertIn("Issue #1", readme)
        self.assertIn("https://github.com/jaabster-dev/u-gas", (ROOT / "templates/pica/AGENTS.md").read_text(encoding="utf-8"))

    def test_public_files_have_no_private_markers(self):
        forbidden = re.compile(r"/" + "Users/" + r"|~/" + "Documents/GitHub|" + "gh" + "p_|" + "github_" + "pat_|BEGIN [A-Z ]*PRIVATE KEY")
        for path in ROOT.rglob("*.md"):
            if ".git" not in path.parts:
                self.assertIsNone(forbidden.search(path.read_text(encoding="utf-8")), str(path))


if __name__ == "__main__":
    unittest.main()
