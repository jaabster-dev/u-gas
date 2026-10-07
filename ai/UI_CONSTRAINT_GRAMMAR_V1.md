# U-GAS UI Constraint Grammar v1

## Purpose

Make the smallest proven subset of `ai/UI_CONSTRAINT_MODEL.md` executable without turning U-GAS into a universal UI DSL.

The conceptual model remains semantic authority. This grammar is a portable machine-authority adapter for bounded responsive surfaces where deterministic solving and invariant verification reduce implementation ambiguity.

Files:

- schema: `ai/ui-constraint-model-v1.schema.json`;
- validator/solver: `scripts/check_ui_constraints.py`;
- portable regression tests: `tests/test_ui_constraint_model.py`.

## Accepted v1 semantics

V1 accepts:

- stable node identity and semantic role;
- separate semantic, layout, and focus-parent references;
- declared box semantics and per-axis size behavior;
- explicit environment inputs;
- weighted inline row tracks with padding, gap, and optional min/max clamps;
- numeric constants;
- equality anchors over `leading/trailing/top/bottom/width/height/centerX/centerY`;
- `REQUIRED / STRONG / PREFERRED / FALLBACK` strengths;
- declared adaptive-transform vocabulary;
- solved observations as evidence;
- relational assertions.

Constraint resolution is deterministic:

1. solve declared track geometry;
2. resolve constants and anchors only when dependencies are available;
3. higher strength wins for the same solvable target;
4. contradictory same-strength assignments invalidate the model;
5. unresolved references or dependency chains fail closed.

## Rejected or deferred from v1

V1 intentionally omits arbitrary formula strings, embedded programming, a general linear/non-linear solver, device-name layout inputs, renderer-specific syntax as design authority, per-breakpoint coordinate tables, screenshot-to-rules inference, automatic conflict repair, and exhaustive design serialization.

Add a primitive only when a real approved surface cannot be expressed safely with the current subset and simpler existing mechanisms have failed. Unsupported semantics remain a specification `GAP`.

## Portable proof boundary

The public distribution uses a synthetic two-pane regression fixture. It verifies that one relational model solves multiple observations, min/max track clamping redistributes remaining space deterministically, same-strength conflicts fail closed, stronger constraints override weaker ones, and device names are rejected as environment inputs.

Product-specific evidence remains in the product/GAS authority that performed the dogfood; U-GAS does not need to ship a private or product-bound fixture to preserve the portable contract.

## Standards boundary rechecked 2026-10-07

The v1 freeze was checked against current official Apple adaptable layout/Larger Text guidance, Android adaptive-window/insets/font-scaling guidance, Figma Auto Layout/Constraints guidance, and WCAG 2.2 Reflow/Text Spacing/Meaningful Sequence/Focus Order.

The portable conclusion is narrow:

- available window/container geometry is primary adaptive input;
- safe/system insets can change usable geometry;
- text scale/reflow and localization/RTL can alter layout;
- semantic/read/focus order must survive relevant visual reflow;
- platform guidance constrains behavior but does not supply a universal product visual language.

## Promotion rule

Use v1 only when it closes real ambiguity. Expand it only from demonstrated product need plus tests. Keep structural solver success distinct from rendered, device, and owner visual acceptance.

`GRAMMAR PASS != VISUAL PASS != PRODUCTION PASS`
