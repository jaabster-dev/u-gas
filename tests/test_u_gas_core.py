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
        self.assertIn("U-GAS (Universal Grabbers Agent System)", readme)
        self.assertIn("EXPERIMENTAL", readme)
        self.assertIn("NO INDEPENDENT USER VALIDATION YET", readme)
        self.assertIn("PICA SELF-CHECK", readme)
        self.assertIn("Issue #1", readme)
        self.assertIn("https://github.com/jaabster-dev/u-gas", (ROOT / "templates/pica/AGENTS.md").read_text(encoding="utf-8"))

    def test_readme_human_hierarchy_and_pica_order(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("> *The conversation can be temporary; the project state is not.*", readme)
        self.assertIn("flowchart LR", readme)
        self.assertLess(readme.index("### A typical workflow"), readme.index("## Quick Start"))
        self.assertLess(readme.index("## How U-GAS works"), readme.index("## Safety and limitations"))
        self.assertLess(readme.index("`PROGRESS.md` — P"), readme.index("`IDEAS.md` — I"))
        self.assertLess(readme.index("`IDEAS.md` — I"), readme.index("`CURRENT_STATE.md` — C"))
        self.assertLess(readme.index("`CURRENT_STATE.md` — C"), readme.index("`AGENTS.md` — A"))
        self.assertLess(readme.index("- PROGRESS.md: PRESENT"), readme.index("- IDEAS.md: PRESENT"))
        self.assertLess(readme.index("- IDEAS.md: PRESENT"), readme.index("- CURRENT_STATE.md: PRESENT"))
        self.assertLess(readme.index("- CURRENT_STATE.md: PRESENT"), readme.index("- AGENTS.md: PRESENT"))
        self.assertLess(readme.index("PROGRESS.md, IDEAS.md, CURRENT_STATE.md, and AGENTS.md"), readme.index("PICA SELF-CHECK"))

    def test_pica_agents_have_identity_haiku(self):
        haiku = "> Clear paths guide the work<br>\n> State remains where agents meet<br>\n> Truth survives each handoff"
        for relative in ("AGENTS.md", "templates/pica/AGENTS.md", "examples/first-project/AGENTS.md"):
            self.assertIn(haiku, (ROOT / relative).read_text(encoding="utf-8"), relative)

    def test_public_files_have_no_private_markers(self):
        forbidden = re.compile(r"/" + "Users/" + r"|~/" + "Documents/GitHub|" + "gh" + "p_|" + "github_" + "pat_|BEGIN [A-Z ]*PRIVATE KEY")
        for path in ROOT.rglob("*.md"):
            if ".git" not in path.parts:
                self.assertIsNone(forbidden.search(path.read_text(encoding="utf-8")), str(path))

    def test_long_handoff_surface_is_present_and_generic(self):
        readme = (ROOT / "handoffs/README.md").read_text(encoding="utf-8")
        checker = (ROOT / "scripts/check_handoff.py").read_text(encoding="utf-8")
        self.assertIn("Compact one-copy handoffs remain the normal path", readme)
        self.assertIn("exact target assertion", readme)
        self.assertNotIn("GrabbersApp", checker)


if __name__ == "__main__":
    unittest.main()
