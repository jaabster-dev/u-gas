#!/usr/bin/env python3
from __future__ import annotations

import copy
import unittest

import scripts.check_ui_constraints as ui


def sample_model():
    return {
        "schemaVersion": 1,
        "surface": {"id": "portable.two-pane", "state": "default"},
        "authority": {
            "repository": "example/example",
            "figmaFileKey": "abcdefghijklmnopqrstuv",
            "note": "Synthetic portability fixture; no product authority."
        },
        "environment": {"inputs": ["availableWidth", "availableHeight"]},
        "nodes": [
            {"id": "root", "role": "screen", "boxes": ["layout"], "inlineSize": "fill", "blockSize": "fill"},
            {"id": "primary", "role": "pane", "semanticParent": "root", "layoutParent": "root", "boxes": ["layout"], "inlineSize": "clamped", "blockSize": "fill"},
            {"id": "secondary", "role": "pane", "semanticParent": "root", "layoutParent": "root", "boxes": ["layout"], "inlineSize": "elastic", "blockSize": "fill"},
            {"id": "action", "role": "primary-action", "semanticParent": "primary", "layoutParent": "primary", "focusParent": "primary", "boxes": ["visual", "layout", "interaction", "focus"], "inlineSize": "fill", "blockSize": "fixed"}
        ],
        "layout": {
            "rowTracks": [{
                "container": "root",
                "paddingLeading": 20,
                "paddingTrailing": 20,
                "gap": 12,
                "tracks": [
                    {"node": "primary", "weight": 1, "max": 300},
                    {"node": "secondary", "weight": 1}
                ],
                "strength": "REQUIRED"
            }],
            "constants": [
                {"target": "action.height", "value": 44, "strength": "REQUIRED"}
            ],
            "anchors": [
                {"target": "primary.top", "source": "root.top", "offset": 0, "strength": "REQUIRED"},
                {"target": "primary.bottom", "source": "root.bottom", "offset": 0, "strength": "REQUIRED"},
                {"target": "secondary.top", "source": "root.top", "offset": 0, "strength": "REQUIRED"},
                {"target": "secondary.bottom", "source": "root.bottom", "offset": 0, "strength": "REQUIRED"},
                {"target": "action.leading", "source": "primary.leading", "offset": 0, "strength": "REQUIRED"},
                {"target": "action.trailing", "source": "primary.trailing", "offset": 0, "strength": "REQUIRED"},
                {"target": "action.bottom", "source": "root.bottom", "offset": -20, "strength": "REQUIRED"}
            ],
            "transforms": [
                {"node": "primary", "type": "RESIZE", "cause": "available geometry"},
                {"node": "secondary", "type": "RESIZE", "cause": "available geometry"}
            ]
        },
        "observations": [
            {
                "id": "narrow",
                "figmaNode": "1:1",
                "environment": {"availableWidth": 600, "availableHeight": 500},
                "expectedGeometry": {
                    "primary": {"leading": 20, "width": 274},
                    "secondary": {"leading": 306, "width": 274},
                    "action": {"leading": 20, "top": 436, "width": 274, "height": 44}
                }
            },
            {
                "id": "wide",
                "figmaNode": "1:2",
                "environment": {"availableWidth": 1000, "availableHeight": 500},
                "expectedGeometry": {
                    "primary": {"leading": 20, "width": 300},
                    "secondary": {"leading": 332, "width": 648},
                    "action": {"leading": 20, "top": 436, "width": 300, "height": 44}
                }
            }
        ],
        "assertions": [
            {"target": "secondary.leading", "source": "primary.trailing", "offset": 12, "strength": "REQUIRED"},
            {"target": "action.trailing", "source": "primary.trailing", "offset": 0, "strength": "REQUIRED"}
        ]
    }


class UIConstraintGrammarTests(unittest.TestCase):
    def test_portable_model_solves_multiple_observations(self):
        model = sample_model()
        self.assertEqual(ui.verify_model(model), [])

    def test_same_strength_conflict_fails_closed(self):
        model = sample_model()
        model["layout"]["constants"].append({"target": "action.height", "value": 45, "strength": "REQUIRED"})
        with self.assertRaises(ui.ModelError):
            ui.solve(model, model["observations"][0]["environment"])

    def test_stronger_rule_wins_without_order_dependence(self):
        model = sample_model()
        model["layout"]["constants"].insert(0, {"target": "action.height", "value": 40, "strength": "FALLBACK"})
        solved = ui.solve(model, model["observations"][0]["environment"])
        self.assertEqual(solved["action"]["height"], 44)

    def test_device_name_input_is_rejected(self):
        model = sample_model()
        model["environment"]["inputs"].append("tablet")
        with self.assertRaises(ui.ModelError):
            ui.validate_model(model)


if __name__ == "__main__":
    unittest.main()
