#!/usr/bin/env python3
"""Validate and solve the bounded GAS UI Constraint Grammar v1."""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

SCHEMA_VERSION = 1
BOXES = {"visual", "layout", "text-flow", "clip", "interaction", "focus", "safe-content"}
SIZE_BEHAVIORS = {"fixed", "intrinsic", "fill", "elastic", "clamped", "wrap", "scroll", "aspect-ratio", "transform-switched"}
STRENGTHS = {"REQUIRED": 4, "STRONG": 3, "PREFERRED": 2, "FALLBACK": 1}
TRANSFORMS = {"PRESERVE", "RESIZE", "REFLOW", "REPOSITION", "REVEAL", "HIDE", "REPLACE", "STACK", "SPLIT", "SCROLL", "PRESENTATION_CHANGE"}
ENV_INPUTS = {"availableWidth", "availableHeight", "safeInsets", "densityOrScale", "textScale", "locale", "layoutDirection", "platform", "inputModality", "windowPosture", "accessibilityPreferences"}
ATTRS = {"leading", "trailing", "top", "bottom", "width", "height", "centerX", "centerY"}


class ModelError(ValueError):
    pass


def _ref_parts(ref):
    if not isinstance(ref, str) or "." not in ref:
        raise ModelError(f"invalid geometry reference: {ref!r}")
    node, attr = ref.rsplit(".", 1)
    if not node or attr not in ATTRS:
        raise ModelError(f"invalid geometry reference: {ref!r}")
    return node, attr


def validate_model(model):
    if model.get("schemaVersion") != SCHEMA_VERSION:
        raise ModelError("unsupported schemaVersion")
    nodes = model.get("nodes")
    if not isinstance(nodes, list) or not nodes:
        raise ModelError("nodes must be a non-empty list")
    ids = []
    for node in nodes:
        if not isinstance(node, dict) or not isinstance(node.get("id"), str) or not node["id"]:
            raise ModelError("every node needs id")
        ids.append(node["id"])
        if not isinstance(node.get("role"), str) or not node["role"]:
            raise ModelError(f"{node['id']}: role required")
        boxes = node.get("boxes", [])
        if not isinstance(boxes, list) or any(box not in BOXES for box in boxes):
            raise ModelError(f"{node['id']}: invalid boxes")
        for key in ("inlineSize", "blockSize"):
            if key in node and node[key] not in SIZE_BEHAVIORS:
                raise ModelError(f"{node['id']}: invalid {key}")
        visibility = node.get("visibleWhen")
        if visibility is not None and (
            not isinstance(visibility, dict)
            or not isinstance(visibility.get("stateKey"), str)
            or not visibility["stateKey"]
            or not isinstance(visibility.get("equals"), str)
            or not visibility["equals"]
            or set(visibility) != {"stateKey", "equals"}
        ):
            raise ModelError(f"{node['id']}: invalid visibleWhen")
    if len(ids) != len(set(ids)):
        raise ModelError("duplicate node id")
    node_ids = set(ids)
    if "root" not in node_ids:
        raise ModelError("root node required")
    for node in nodes:
        for key in ("semanticParent", "layoutParent", "focusParent"):
            if key in node and node[key] is not None and node[key] not in node_ids:
                raise ModelError(f"{node['id']}: unknown {key}")

    inputs = model.get("environment", {}).get("inputs", [])
    if not isinstance(inputs, list) or any(item not in ENV_INPUTS for item in inputs):
        raise ModelError("invalid environment inputs")

    layout = model.get("layout")
    if not isinstance(layout, dict):
        raise ModelError("layout required")
    for row in layout.get("rowTracks", []):
        if row.get("container") not in node_ids:
            raise ModelError("rowTracks container unknown")
        if row.get("strength") not in STRENGTHS:
            raise ModelError("rowTracks strength invalid")
        tracks = row.get("tracks")
        if not isinstance(tracks, list) or not tracks:
            raise ModelError("rowTracks tracks required")
        for track in tracks:
            if track.get("node") not in node_ids:
                raise ModelError("rowTracks node unknown")
            if not isinstance(track.get("weight"), (int, float)) or track["weight"] <= 0:
                raise ModelError("rowTracks weight must be positive")
            if "min" in track and "max" in track and track["min"] > track["max"]:
                raise ModelError("track min > max")

    for group in ("constants", "anchors"):
        for constraint in layout.get(group, []):
            if constraint.get("strength") not in STRENGTHS:
                raise ModelError(f"{group}: invalid strength")
            node, _ = _ref_parts(constraint.get("target"))
            if node not in node_ids:
                raise ModelError(f"{group}: target node unknown")
            if group == "anchors":
                node, _ = _ref_parts(constraint.get("source"))
                if node not in node_ids:
                    raise ModelError("anchors: source node unknown")

    for transform in layout.get("transforms", []):
        if transform.get("node") not in node_ids or transform.get("type") not in TRANSFORMS:
            raise ModelError("invalid transform")

    state_invariants = layout.get("stateInvariants", [])
    if not isinstance(state_invariants, list):
        raise ModelError("stateInvariants must be a list")
    invariant_ids = []
    for invariant in state_invariants:
        if not isinstance(invariant, dict):
            raise ModelError("state invariant must be an object")
        invariant_ids.append(invariant.get("id"))
        if (set(invariant) != {"id", "stateKey", "values", "nodes", "attributes", "strength"}
                or not isinstance(invariant.get("stateKey"), str) or not invariant["stateKey"]
                or not isinstance(invariant.get("values"), list) or len(invariant["values"]) < 2
                or any(not isinstance(value, str) or not value for value in invariant["values"])
                or len(invariant["values"]) != len(set(invariant["values"]))
                or not isinstance(invariant.get("nodes"), list) or not invariant["nodes"]
                or any(node not in node_ids for node in invariant["nodes"])
                or len(invariant["nodes"]) != len(set(invariant["nodes"]))
                or not isinstance(invariant.get("attributes"), list) or not invariant["attributes"]
                or any(attr not in ATTRS for attr in invariant["attributes"])
                or len(invariant["attributes"]) != len(set(invariant["attributes"]))
                or invariant.get("strength") not in STRENGTHS):
            raise ModelError("invalid state invariant")
    if len(invariant_ids) != len(set(invariant_ids)) or any(not isinstance(i, str) or not i for i in invariant_ids):
        raise ModelError("state invariant ids must be unique non-empty strings")

    observations = model.get("observations")
    if not isinstance(observations, list) or not observations:
        raise ModelError("observations required")
    for observation in observations:
        env = observation.get("environment", {})
        for required in ("availableWidth", "availableHeight"):
            if not isinstance(env.get(required), (int, float)) or env[required] <= 0:
                raise ModelError(f"observation {observation.get('id')}: {required} required")
        expected = observation.get("expectedGeometry", {})
        state = observation.get("state", {})
        if not isinstance(state, dict) or any(not isinstance(k, str) or not k or not isinstance(v, str) or not v for k, v in state.items()):
            raise ModelError(f"observation {observation.get('id')}: invalid state")
        for node, attrs in expected.items():
            if node not in node_ids:
                raise ModelError(f"observation {observation.get('id')}: unknown node {node}")
            if not isinstance(attrs, dict) or any(key not in ATTRS or not isinstance(value, (int, float)) for key, value in attrs.items()):
                raise ModelError(f"observation {observation.get('id')}: invalid geometry")
        for node in nodes:
            condition = node.get("visibleWhen")
            if condition is None:
                continue
            key = condition["stateKey"]
            if key not in state:
                raise ModelError(f"observation {observation.get('id')}: missing visibility state {key}")
            is_visible = state[key] == condition["equals"]
            if (node["id"] in expected) != is_visible:
                raise ModelError(f"observation {observation.get('id')}: {node['id']} visibility disagrees with state")

    for assertion in model.get("assertions", []):
        if assertion.get("strength") not in STRENGTHS:
            raise ModelError("assertion strength invalid")
        for key in ("target", "source"):
            node, _ = _ref_parts(assertion.get(key))
            if node not in node_ids:
                raise ModelError(f"assertion {key} node unknown")
    return model


def verify_state_invariants(model, tolerance=1e-6):
    """Require paired observations to preserve selected measured geometry."""
    observations = model.get("observations", [])
    failures = []
    for invariant in model.get("layout", {}).get("stateInvariants", []):
        key = invariant["stateKey"]
        groups = defaultdict(dict)
        for observation in observations:
            state = observation.get("state", {})
            if key not in state or state[key] not in invariant["values"]:
                continue
            context = (json.dumps(observation.get("environment", {}), sort_keys=True),
                       json.dumps({k: v for k, v in state.items() if k != key}, sort_keys=True))
            value = state[key]
            if value in groups[context]:
                raise ModelError(f"state invariant {invariant['id']}: duplicate observation for {value}")
            groups[context][value] = observation
        if not groups:
            raise ModelError(f"state invariant {invariant['id']}: no paired observations")
        for context, pair in groups.items():
            if set(pair) != set(invariant["values"]):
                raise ModelError(f"state invariant {invariant['id']}: incomplete state pair")
            baseline = pair[invariant["values"][0]]
            for value in invariant["values"][1:]:
                other = pair[value]
                for node in invariant["nodes"]:
                    for attr in invariant["attributes"]:
                        left = baseline.get("expectedGeometry", {}).get(node, {}).get(attr)
                        right = other.get("expectedGeometry", {}).get(node, {}).get(attr)
                        if left is None or right is None:
                            raise ModelError(f"state invariant {invariant['id']}: missing {node}.{attr}")
                        if abs(left - right) > tolerance:
                            failures.append(f"{invariant['id']} {node}.{attr}: {baseline['id']}={left} vs {other['id']}={right}")
    return failures


def _derived(geometry, attr):
    if attr in geometry:
        return geometry[attr]
    if attr == "trailing" and "leading" in geometry and "width" in geometry:
        return geometry["leading"] + geometry["width"]
    if attr == "bottom" and "top" in geometry and "height" in geometry:
        return geometry["top"] + geometry["height"]
    if attr == "centerX" and "leading" in geometry and "width" in geometry:
        return geometry["leading"] + geometry["width"] / 2
    if attr == "centerY" and "top" in geometry and "height" in geometry:
        return geometry["top"] + geometry["height"] / 2
    return None


def _apply_value(geometry, attr, value):
    if attr in {"leading", "top", "width", "height"}:
        geometry[attr] = value
        return True
    if attr == "trailing":
        if "width" in geometry:
            geometry["leading"] = value - geometry["width"]
            return True
        if "leading" in geometry:
            geometry["width"] = value - geometry["leading"]
            return True
    if attr == "bottom":
        if "height" in geometry:
            geometry["top"] = value - geometry["height"]
            return True
        if "top" in geometry:
            geometry["height"] = value - geometry["top"]
            return True
    if attr == "centerX" and "width" in geometry:
        geometry["leading"] = value - geometry["width"] / 2
        return True
    if attr == "centerY" and "height" in geometry:
        geometry["top"] = value - geometry["height"] / 2
        return True
    return False


def _set(assignments, geometry, target, value, strength, source):
    node, attr = _ref_parts(target)
    rank = STRENGTHS[strength]
    old = assignments.get(target)
    if old:
        old_value, old_rank, old_source = old
        if rank < old_rank:
            return False
        if rank == old_rank:
            if abs(old_value - value) > 1e-7:
                raise ModelError(f"conflict at {target}: {old_source}={old_value} vs {source}={value}")
            return False
    if not _apply_value(geometry[node], attr, value):
        return False
    assignments[target] = (value, rank, source)
    return True


def _solve_tracks(row, root_width, geometry, assignments):
    tracks = [dict(track) for track in row["tracks"]]
    available = root_width - row.get("paddingLeading", 0) - row.get("paddingTrailing", 0) - row.get("gap", 0) * (len(tracks) - 1)
    if available < 0:
        raise ModelError("negative row track space")
    unresolved = set(range(len(tracks)))
    widths = [0.0] * len(tracks)
    remaining = available
    while unresolved:
        weight = sum(tracks[index]["weight"] for index in unresolved)
        if weight <= 0:
            raise ModelError("invalid row track weight")
        changed = False
        for index in list(unresolved):
            proposal = remaining * tracks[index]["weight"] / weight
            minimum = tracks[index].get("min")
            maximum = tracks[index].get("max")
            if minimum is not None and proposal < minimum:
                widths[index] = float(minimum)
                remaining -= widths[index]
                unresolved.remove(index)
                changed = True
            elif maximum is not None and proposal > maximum:
                widths[index] = float(maximum)
                remaining -= widths[index]
                unresolved.remove(index)
                changed = True
        if not changed:
            weight = sum(tracks[index]["weight"] for index in unresolved)
            for index in unresolved:
                widths[index] = remaining * tracks[index]["weight"] / weight
            unresolved.clear()
    if remaining < -1e-7:
        raise ModelError("row track minimums exceed available width")

    leading = float(row.get("paddingLeading", 0))
    for index, track in enumerate(tracks):
        _set(assignments, geometry, f"{track['node']}.leading", leading, row["strength"], "rowTracks")
        _set(assignments, geometry, f"{track['node']}.width", widths[index], row["strength"], "rowTracks")
        leading += widths[index] + (row.get("gap", 0) if index < len(tracks) - 1 else 0)


def solve(model, environment):
    validate_model(model)
    width = float(environment["availableWidth"])
    height = float(environment["availableHeight"])
    geometry = {node["id"]: {} for node in model["nodes"]}
    geometry["root"] = {"leading": 0.0, "top": 0.0, "width": width, "height": height}
    assignments = {}

    for row in model["layout"].get("rowTracks", []):
        _solve_tracks(row, width, geometry, assignments)

    pending = [("constant", item) for item in model["layout"].get("constants", [])]
    pending += [("anchor", item) for item in model["layout"].get("anchors", [])]
    for _ in range(max(4, len(pending) * 3)):
        progress = False
        next_pending = []
        for kind, constraint in pending:
            if kind == "constant":
                _set(assignments, geometry, constraint["target"], float(constraint["value"]), constraint["strength"], "constant")
                node, attr = _ref_parts(constraint["target"])
                if _derived(geometry[node], attr) is None:
                    next_pending.append((kind, constraint))
                else:
                    progress = True
            else:
                source_node, source_attr = _ref_parts(constraint["source"])
                value = _derived(geometry[source_node], source_attr)
                if value is None:
                    next_pending.append((kind, constraint))
                    continue
                target_value = value + float(constraint.get("offset", 0))
                _set(assignments, geometry, constraint["target"], target_value, constraint["strength"], f"anchor:{constraint['source']}")
                target_node, target_attr = _ref_parts(constraint["target"])
                if _derived(geometry[target_node], target_attr) is None:
                    next_pending.append((kind, constraint))
                else:
                    progress = True
        pending = next_pending
        if not pending:
            break
        if not progress:
            break
    if pending:
        unresolved = ", ".join(constraint["target"] for _, constraint in pending)
        raise ModelError(f"unresolved constraints: {unresolved}")
    return geometry


def verify_observation(model, observation, tolerance=1e-6):
    geometry = solve(model, observation["environment"])
    failures = []
    for node, expected in observation["expectedGeometry"].items():
        for attr, wanted in expected.items():
            got = _derived(geometry[node], attr)
            if got is None or abs(got - wanted) > tolerance:
                failures.append(f"{observation['id']} {node}.{attr}: expected {wanted}, got {got}")
    for assertion in model.get("assertions", []):
        target_node, target_attr = _ref_parts(assertion["target"])
        source_node, source_attr = _ref_parts(assertion["source"])
        left = _derived(geometry[target_node], target_attr)
        right = _derived(geometry[source_node], source_attr)
        wanted = None if right is None else right + float(assertion.get("offset", 0))
        if left is None or wanted is None or abs(left - wanted) > tolerance:
            failures.append(
                f"{observation['id']} assertion {assertion['target']} == {assertion['source']} + {assertion.get('offset', 0)} failed"
            )
    return failures


def verify_model(model):
    validate_model(model)
    failures = []
    for observation in model["observations"]:
        failures.extend(verify_observation(model, observation))
    failures.extend(verify_state_invariants(model))
    return failures


def load_model(path):
    return validate_model(json.loads(Path(path).read_text(encoding="utf-8")))


if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model", type=Path)
    args = parser.parse_args()
    try:
        loaded = load_model(args.model)
        failures = verify_model(loaded)
    except (OSError, json.JSONDecodeError, ModelError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        raise SystemExit(1)
    print(f"PASS: {args.model} ({len(loaded['observations'])} observations)")
