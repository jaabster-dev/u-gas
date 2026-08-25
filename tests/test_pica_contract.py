import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from pica_contract import CANONICAL_UPSTREAM, PICA_FILES, load_templates, missing_pica, preserve_substantive


class PicaContractTests(unittest.TestCase):
    def test_exact_four_filenames(self):
        self.assertEqual(PICA_FILES, ("AGENTS.md", "CURRENT_STATE.md", "PROGRESS.md", "IDEAS.md"))

    def test_templates_load_and_are_complete(self):
        templates = load_templates(ROOT)
        self.assertEqual(set(templates), set(PICA_FILES))
        self.assertIn(CANONICAL_UPSTREAM, templates["AGENTS.md"])
        self.assertIn("Quiet page at dawn", templates["CURRENT_STATE.md"])
        self.assertIn("Footprints wait in snow", templates["PROGRESS.md"])
        self.assertIn("Empty shelf, open", templates["IDEAS.md"])

    def test_missing_detection(self):
        self.assertEqual(missing_pica(["AGENTS.md", "IDEAS.md"]), ["CURRENT_STATE.md", "PROGRESS.md"])

    def test_existing_content_is_never_overwritten_by_helper(self):
        existing = "# Existing substantive control\n"
        self.assertEqual(preserve_substantive(existing, "template"), existing)
        self.assertEqual(preserve_substantive(None, "template"), "template")


if __name__ == "__main__":
    unittest.main()
