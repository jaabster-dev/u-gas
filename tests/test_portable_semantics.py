import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_u_gas import current_state_review


class PortableSemanticsTests(unittest.TestCase):
    def read(self, relative):
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_direct_first_capability_routing_is_explicit(self):
        agents = self.read("AGENTS.md")
        self.assertIn("least expensive currently authorized capability", agents)
        self.assertIn("direct repository/file/tool access before escalation", agents)
        self.assertIn("material missing capability", agents)

    def test_scope_control_and_changed_file_relevance_are_explicit(self):
        governance = self.read("ai/GOVERNANCE.md")
        workflow = self.read("ai/GITHUB_WORKFLOW.md")
        for marker in ("compact task contract", "objective", "accepted scope", "non-goals", "required verification"):
            self.assertIn(marker, governance)
        self.assertIn("scope reset", workflow)
        self.assertIn("every changed file must be relevant", workflow)
        self.assertIn("parked ideas", workflow)

    def test_selective_bootstrap_is_explicit(self):
        continuity = self.read("ai/SESSION_CONTINUITY.md")
        self.assertIn("Cold/successor/resume work", continuity)
        self.assertIn("Ordinary active-session follow-ups do not mechanically cold-bootstrap", continuity)

    def test_current_state_lifecycle_hygiene_is_explicit(self):
        continuity = self.read("ai/SESSION_CONTINUITY.md")
        structure = self.read("ai/REPOSITORY_STRUCTURE.md")
        for marker in ("compact live resume surface", "evidence-triggered", "partial or truncated history"):
            self.assertIn(marker, continuity)
        self.assertIn("compact live resume surface", structure)
        self.assertIn("paused/deferred return conditions", structure)
        self.assertIn("partial history read", structure)

    def test_current_state_review_is_read_only_signal(self):
        before = (ROOT / "CURRENT_STATE.md").read_bytes()
        self.assertIn(current_state_review(ROOT), ("PASS", "REVIEW"))
        after = (ROOT / "CURRENT_STATE.md").read_bytes()
        self.assertEqual(before, after)

    def test_compliance_declares_semantic_regression_coverage(self):
        compliance = self.read("ai/COMPLIANCE.md")
        for marker in (
            "direct-first capability routing",
            "scope reset/changed-file relevance",
            "selective bootstrap",
            "compact current-state lifecycle semantics",
            "CURRENT_STATE_REVIEW",
            "read-only diagnostic signal",
            "not itself a compliance failure",
        ):
            self.assertIn(marker, compliance)


if __name__ == "__main__":
    unittest.main()
