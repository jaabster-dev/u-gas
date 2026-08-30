import pathlib
import re
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_u_gas import AI_FILES, SKILL_FILES, REQUIRED_SKILL_SECTIONS, check_distribution, skill_structure_errors


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

    def test_all_public_skills_have_operational_structure(self):
        for relative in SKILL_FILES:
            text = (ROOT / relative).read_text(encoding="utf-8")
            self.assertEqual(skill_structure_errors(relative, text), [], relative)
            for section in REQUIRED_SKILL_SECTIONS:
                self.assertIn(f"## {section}", text, relative)

    def test_rebuilt_skills_retain_operational_markers(self):
        expected = {
            "skills/u-gas-resume/SKILL.md": ("RESUME ACTION", "PROJECT NEXT", "CURRENT_STATE.md", "WAITING/PAUSED", "read-back"),
            "skills/u-gas-safe-patch/SKILL.md": ("PARTIAL READ", "BLOCKED", "authoritative", "bounded", "idempotency"),
            "skills/u-gas-verify-change/SKILL.md": ("REQUIREMENT", "ACTUAL DIFF", "REQUIRED TESTS", "REQUIRED EVIDENCE", "PASS", "FAIL", "human verification", "not itself proof", "rendered", "structural evidence only", "source identity", "visual correctness", "unverified", "not a Figma-specific subsystem"),
            "skills/u-gas-external-research/SKILL.md": ("research/evidence, not authority", "observed fact", "inference", "dependency", "security", "license", "u-gas-skill-review", "acceptance chain", "killer assumptions", "cheapest safe pre-flight", "UNKNOWN", "buildability is not acceptance evidence"),
        }
        for relative, markers in expected.items():
            text = (ROOT / relative).read_text(encoding="utf-8").lower()
            for marker in markers:
                self.assertIn(marker.lower(), text, f"{relative}: {marker}")

    def test_skill_review_requires_end_to_end_operational_contract(self):
        text = (ROOT / "skills/u-gas-skill-review/SKILL.md").read_text(encoding="utf-8").lower()
        required_patterns = (
            r"trigger.*non-trigger|non-trigger.*trigger",
            r"input.*precondition|precondition.*input",
            r"ordered.*procedure|procedure.*ordered",
            r"reference.*tool.*authority|authority.*reference.*tool",
            r"decision.*failure.*fail-closed|fail-closed.*decision.*failure",
            r"verif(?:iable|ied).*completion.*outcome|completion.*outcome.*verif",
            r"competent agent.*execute.*capability.*verified result",
            r"operationally incomplete",
            r"adopt",
        )
        for pattern in required_patterns:
            self.assertRegex(text, pattern, pattern)
        for verdict in ("adapt principle", "adopt", "build internal", "reject"):
            self.assertIn(verdict, text)
        self.assertRegex(text, r"not (?:return|allow).*adopt.*(?:gap|incomplete|unresolved)")

    def test_critical_path_sanity_pause_is_agent_owned_and_fail_visible(self):
        governance = (ROOT / "ai/GOVERNANCE.md").read_text(encoding="utf-8").lower()
        for marker in (
            "materially costly or dependency-heavy",
            "killer assumptions",
            "later hard gates",
            "cheapest pre-flight",
            "simpler existing route",
            "intermediate solution",
            "agent-owned reasoning",
            "not human approval",
            "unknown",
            "ordinary bounded work",
        ):
            self.assertIn(marker, governance, marker)

    def test_multi_agent_policy_has_operational_boundaries(self):
        policy = (ROOT / "ai/MULTI_AGENT_COLLABORATION.md").read_text(encoding="utf-8")
        for marker in (
            "multiple agents, sessions, or executors",
            "Do not invoke a heavy collaboration protocol",
            "shared coordination surface",
            "preserve unique",
            "reconcile",
            "fail closed",
            "one coherent authoritative result",
        ):
            self.assertIn(marker, policy)

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
        self.assertIn("<summary>Manual fallback: continue an existing project</summary>", readme)
        self.assertLess(readme.index("### Start a new local project — recommended first test"), readme.index("<summary>Manual fallback: continue an existing project</summary>"))
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
        self.assertIn("Ordinary ChatGPT and Codex on", readme)
        self.assertIn("credits, plans, entitlements", readme)
        self.assertIn("routine\nTerminal/Git/file-transfer work", readme)
        self.assertIn("provider/session storage", governance)
        normalized = " ".join(readme.split())
        self.assertIn("immediately show one prominent `NEXT ACTION`", normalized)
        self.assertIn("you should not choose routine execution mechanics", normalized)

    def test_public_starter_promotes_only_tested_local_route(self):
        starter = (ROOT / "starter/index.html").read_text(encoding="utf-8")
        self.assertIn("PUBLIC STARTER", starter)
        self.assertIn('value="computer" checked', starter)
        self.assertIn('value="github" disabled', starter)
        self.assertIn('value="cloud" disabled', starter)
        self.assertIn("~/Documents/U-GAS Projects/", starter)
        self.assertIn("GIVE THIS TO YOUR NEXT AI CHAT.txt", starter)
        self.assertIn("https://github.com/jaabster-dev/u-gas", starter)
        self.assertIn("Made with U-GAS by ĀBŌ", starter)
        self.assertIn("Copy this complete result and paste it back into the AI chat that sent you here.", starter)
        self.assertIn("Codex is a tested example, not mandatory", starter)
        self.assertIn("immediately expose one prominent NEXT ACTION naming that executor", starter)
        self.assertIn("Do not present routine execution choices or ask the owner how to proceed", starter)

    def test_public_starter_first_contact_destination_contract(self):
        starter = (ROOT / "starter/index.html").read_text(encoding="utf-8")
        self.assertIn("U-GAS helps your AI build and continue a project without losing its place", starter)
        self.assertIn('id="nextStep"', starter)
        self.assertIn("NEXT STEP", starter)
        self.assertIn("Your prompt is copied.", starter)
        self.assertIn("Open your AI chat, paste it, and send it.", starter)
        self.assertIn('href="https://chatgpt.com/"', starter)
        self.assertIn('href="https://claude.ai/"', starter)
        self.assertIn("Open ChatGPT", starter)
        self.assertIn("Open Claude", starter)
        self.assertIn("Other AI", starter)
        self.assertIn("does not automatically paste or send your prompt", starter)
        self.assertIn("Codex, Claude Code, or another suitable executor", starter)
        self.assertIn("value=\"github\" disabled", starter)
        self.assertIn("value=\"cloud\" disabled", starter)

    def test_public_starter_is_linked_from_action_first_readme(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("https://jaabster-dev.github.io/u-gas/starter/", readme)
        self.assertNotIn("[Project Starter](starter/)", readme)
        self.assertIn('target="_blank"', readme)
        self.assertIn('rel="noopener noreferrer"', readme)
        self.assertLess(readme.index("### How to use it"), readme.index("## How U-GAS works"))
        self.assertIn("one complete copyable handoff", readme)
        self.assertIn("exact file, project path, or verified browser URL", readme)

    def test_resume_and_executor_return_contract(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        governance = (ROOT / "ai/GOVERNANCE.md").read_text(encoding="utf-8")
        for text in (readme, governance):
            self.assertIn("GIVE THIS TO YOUR NEXT AI CHAT.txt", text)
            self.assertIn("not a fifth PICA", text)
            self.assertIn("next useful action", text)
            self.assertIn("restart", text)
        self.assertIn("Copy this complete result and paste it back into the AI chat that sent you here.", governance)
        self.assertIn("actual PICA/project state", " ".join(readme.split()))

    def test_action_first_onboarding_contract(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("### How to use it", readme)
        actions = (
            "starting a new project or continuing one you already have",
            "Describe the project and the outcome you want",
            "If local execution is genuinely needed",
            "Copy the executor's complete result back into the coordinating AI chat",
        )
        for action in actions:
            self.assertIn(action, readme)
        self.assertLess(readme.index("### How to use it"), readme.index("## How U-GAS works"))
        self.assertEqual(readme.count("https://github.com/jaabster-dev/u-gas/issues/1"), 1)
        self.assertEqual(readme.count("GIVE THIS TO YOUR NEXT AI CHAT.txt"), 2)
        current = (ROOT / "CURRENT_STATE.md").read_text(encoding="utf-8")
        self.assertIn("PICA, governance, capability discovery", current)
        self.assertIn("BMAD and GitHub Spec Kit", current)

    def test_public_project_starter_route_contract(self):
        starter = (ROOT / "starter/index.html").read_text(encoding="utf-8")
        starter_readme = (ROOT / "starter/README.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("https://jaabster-dev.github.io/u-gas/starter/", readme)
        self.assertIn('value="computer" checked', starter)
        self.assertIn('value="github" disabled', starter)
        self.assertIn('value="cloud" disabled', starter)

    def test_public_starter_existing_project_mode_and_generated_prompt(self):
        starter = (ROOT / "starter/index.html").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn('name="projectMode" value="new" checked', starter)
        self.assertIn('name="projectMode" value="existing"', starter)
        for field_id in (
            "existingLocation",
            "existingLocationUnknown",
            "existingPurpose",
            "existingGoal",
            "existingObstacle",
            "existingPreserve",
        ):
            self.assertIn(f'id="{field_id}"', starter)
        self.assertIn("If this project is already open in Codex", starter)
        self.assertIn("follow the single NEXT ACTION", starter)
        self.assertIn("You do not need to supply Git commands", readme)

        template_match = re.search(
            r'<template id="existingPromptTemplate">(.*?)</template>', starter, re.S
        )
        self.assertIsNotNone(template_match)
        values = {
            "projectName": "Flashcard Generator",
            "projectLocation": "~/Documents/Flashcard Generator",
            "projectPurpose": "Turn pasted notes into study flashcards.",
            "currentGoal": "Import the next deck without breaking existing behavior.",
            "currentObstacle": "Routine agent work became slow after accumulated safeguards.",
            "mustPreserve": "Saved decks, import behavior, tests, history, and working changes.",
        }
        rendered = re.sub(
            r"\{\{(\w+)\}\}", lambda match: values[match.group(1)], template_match.group(1)
        )
        self.assertIn("EXISTING PROJECT", rendered)
        self.assertIn(values["currentGoal"], rendered)
        for semantic_marker in (
            "Inspect the actual existing project",
            "Do not create a duplicate project",
            "Preserve existing code, history, uncommitted changes, untracked files, unpushed work",
            "add only the minimum missing PICA controls",
            "Do not restart, rewrite, redesign, migrate, broadly clean up, or simplify",
            "Distinguish required safeguards from redundant or risk-disproportionate ceremony",
            "smallest safe next action",
            "Do not remove protections without project-specific evidence",
            "PICA/bootstrap completion is not completion of the project request",
            "Verify the actual repository/workspace state",
        ):
            self.assertIn(semantic_marker, rendered)
        for owner_question in (
            "branch names",
            "commit identifiers",
            "status output",
            "PICA terminology",
            "test commands",
            "architecture",
            "merge mechanics",
        ):
            self.assertIn(owner_question, rendered)

    def test_public_starter_privacy_first_usage_analytics_contract(self):
        starter = (ROOT / "starter/index.html").read_text(encoding="utf-8")
        starter_readme = (ROOT / "starter/README.md").read_text(encoding="utf-8")
        self.assertIn('data-goatcounter="https://u-gas.goatcounter.com/count"', starter)
        self.assertIn('src="https://gc.zgo.at/count.js"', starter)
        self.assertIn("path:'/starter/'", starter)
        self.assertIn("referrer:''", starter)
        self.assertIn("path:'starter-attempt'", starter)
        self.assertIn("title:'Starter attempt'", starter)
        self.assertIn("event:true", starter)
        copy_handler = re.search(r"\$\('copy'\)\.addEventListener\('click',async\(\)=>\{(.*?)\}\);", starter)
        self.assertIsNotNone(copy_handler)
        copy_body = copy_handler.group(1)
        self.assertLess(copy_body.index("await navigator.clipboard.writeText"), copy_body.index("recordStarterAttempt()"))
        self.assertLess(copy_body.index("recordStarterAttempt()"), copy_body.index("status.textContent='Copied.'"))
        self.assertIn("Copy was blocked by this browser.", copy_body)
        self.assertIn("if(result&&typeof result.catch==='function')result.catch(()=>{})", starter)
        self.assertIn("sessionStorage", starter)
        self.assertIn("privacy-friendly aggregate counting", starter_readme)
        self.assertIn("no project or form values", starter_readme)
        self.assertIn("no cookies or fingerprinting", starter_readme)
        event_block = re.search(r"counter\.count\(\{(.*?)\}\)", starter, re.S).group(1)
        for value_name in (
            "name",
            "description",
            "location",
            "customLocation",
            "durableLocation",
            "projectMode",
            "existingLocation",
            "existingPurpose",
            "existingGoal",
            "existingObstacle",
            "existingPreserve",
        ):
            self.assertNotIn(value_name, event_block)
        self.assertIn("~/Documents/U-GAS Projects/", starter)
        self.assertIn("GIVE THIS TO YOUR NEXT AI CHAT.txt", starter)
        self.assertIn("Made with U-GAS by ĀBŌ", starter)
        self.assertIn("PUBLIC STARTER", starter)
        self.assertIn("Back to the U-GAS repository", starter)
        self.assertIn(
            "GitHub and My server / cloud remain visible but disabled",
            " ".join(starter_readme.split()),
        )

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

    def test_pages_deployment_publishes_only_starter(self):
        workflow = (ROOT / ".github/workflows/project-starter-pages.yml").read_text(encoding="utf-8")
        self.assertIn("actions/upload-pages-artifact@v3", workflow)
        self.assertIn("path: _site", workflow)
        self.assertIn("cp -R starter/. _site/starter/", workflow)
        self.assertIn("actions/deploy-pages@v4", workflow)
        self.assertIn("pages: write", workflow)

    def test_agent_identity_canary_and_temporal_grounding_contract(self):
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        continuity = (ROOT / "ai/SESSION_CONTINUITY.md").read_text(encoding="utf-8")
        self.assertIn("low-cost continuity/identity tripwire", agents)
        self.assertIn("not a manual check the user must remember or monitor", agents)
        self.assertIn("actual current local date/time", continuity)
        self.assertIn("today, yesterday, tomorrow", continuity)

    def test_live_obligations_cannot_exist_only_in_progress_history(self):
        continuity = " ".join(
            (ROOT / "ai/SESSION_CONTINUITY.md").read_text(encoding="utf-8").lower().split()
        )
        self.assertRegex(continuity, r"live obligation.*not .*captured.*progress\.md")
        self.assertRegex(continuity, r"unresolved .*current_state\.md|current_state\.md.*unresolved")
        self.assertRegex(continuity, r"progress\.md.*evidence.*history")
        for transition in ("resolved", "deferred", "dropped"):
            self.assertIn(transition, continuity)
        self.assertRegex(continuity, r"progress\.md.*must not be the sole location.*unresolved")


if __name__ == "__main__":
    unittest.main()
