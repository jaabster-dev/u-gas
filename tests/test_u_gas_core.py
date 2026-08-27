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
        self.assertIn("MIT License", readme)
        self.assertIn("Experimental", readme)
        self.assertIn("Tested with ChatGPT", readme)
        self.assertIn("> *The conversation can be temporary; the project state is not.*", readme)
        self.assertNotIn("```mermaid", readme)
        self.assertIn("Plan → Persist → Execute → Verify → Resume", readme)
        self.assertLess(readme.index("## Quick Start"), readme.index("### A typical workflow"))
        self.assertLess(readme.index("## How U-GAS works"), readme.index("## Limitations and safety"))
        self.assertIn("| File | Letter | Answers |", readme)
        self.assertLess(readme.index("| `PROGRESS.md` | P"), readme.index("| `IDEAS.md` | I"))
        self.assertLess(readme.index("| `IDEAS.md` | I"), readme.index("| `CURRENT_STATE.md` | C"))
        self.assertLess(readme.index("| `CURRENT_STATE.md` | C"), readme.index("| `AGENTS.md` | A"))
        self.assertLess(readme.index("- AGENTS.md: PRESENT"), readme.index("- CURRENT_STATE.md: PRESENT"))
        self.assertLess(readme.index("- CURRENT_STATE.md: PRESENT"), readme.index("- PROGRESS.md: PRESENT"))
        self.assertLess(readme.index("- PROGRESS.md: PRESENT"), readme.index("- IDEAS.md: PRESENT"))
        self.assertLess(readme.index("AGENTS.md, CURRENT_STATE.md, PROGRESS.md, IDEAS.md"), readme.index("PICA SELF-CHECK"))

    def test_readme_local_first_onboarding_contract(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertNotIn("Chats fade into night", readme)
        self.assertIn("[Quick Start](#quick-start)", readme)
        self.assertIn("- [How U-GAS works](#how-u-gas-works)", readme)
        self.assertIn("- [Limitations and safety](#limitations-and-safety)", readme)
        self.assertIn("- [Status and feedback](#status-and-feedback)", readme)
        self.assertIn("You do not need to create a GitHub repository.", readme)
        self.assertIn("### Start a new local project — recommended first test", readme)
        self.assertIn("<summary>Already use GitHub?</summary>", readme)
        self.assertLess(readme.index("### Start a new local project — recommended first test"), readme.index("<summary>Already use GitHub?</summary>"))
        self.assertIn("initialize local Git if needed", readme)
        self.assertIn("PICA SELF-CHECK", readme)
        self.assertIn("BLOCKED — persistent filesystem unavailable: <specific capability reason>", readme)
        self.assertIn("Do not create a GitHub repository, remote, account", readme)
        self.assertNotIn("<summary>Copy the complete local-first prompt</summary>", readme)
        self.assertIn("```text\nI want to start a new local U-GAS project.", readme)
        self.assertIn("plain chat with no persistent file access", readme)
        self.assertIn("How to tell if it worked", readme)
        self.assertIn("> [!TIP]", readme)
        self.assertIn("public HTTPS source", readme)
        self.assertIn("Actually try to open and read that public URL", readme)
        normalized = " ".join(readme.split())
        self.assertIn("missing GitHub connector, API access, authenticated integration, or local Git network is not proof", normalized)
        self.assertIn("persistent filesystem unavailable", normalized)
        self.assertIn("local Git unavailable", normalized)
        self.assertIn("Do not probe access with a write", normalized)
        self.assertIn("the setup was not completed", readme)

    def test_readme_execution_escalation_contract(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        governance = (ROOT / "ai/GOVERNANCE.md").read_text(encoding="utf-8")
        for text in (readme, governance):
            self.assertIn("capability discovery", text)
            self.assertIn("one complete", text)
            self.assertIn("Codex", text)
        self.assertIn("not mandatory", governance)
        self.assertIn("ordinary ChatGPT and Codex on", readme)
        self.assertIn("credits, plans, entitlements", readme)
        self.assertIn("routine\nTerminal/Git/file-transfer work", readme)
        self.assertIn("provider/session storage", governance)

    def test_resume_and_executor_return_contract(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        governance = (ROOT / "ai/GOVERNANCE.md").read_text(encoding="utf-8")
        for text in (readme, governance):
            self.assertIn("GIVE THIS TO YOUR NEXT AI CHAT.txt", text)
            self.assertIn("not a fifth PICA", text)
            self.assertIn("Copy this complete result and paste it back into the AI chat that sent you here.", text)
            self.assertIn("next useful action", text)
            self.assertIn("restart", text)
        self.assertIn("actual PICA/project state", " ".join(readme.split()))

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
