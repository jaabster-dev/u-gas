# U-GAS Figma to Production

## Purpose
Implement or reconcile an owner-approved Figma design against an existing production UI while preserving production semantics and verifying what actually renders.

## When to use
Use when current project authority identifies an owner-approved Figma design and an existing production UI must be implemented, reconciled, or diagnosed against it.

## When not to use
Do not use while design authority is still under Figma-only iteration, for greenfield visual invention without approved design authority, or when the task has no production runtime/rendering surface.

## Authority
Current project rules establish design and production authority. Owner-approved Figma defines visual intent; existing production structure defines semantics, accessibility, interaction, and business behavior unless explicitly changed. Runtime computed styles/layout define what actually renders. Required device evidence and owner review remain distinct acceptance layers.

## Constraint-model routing
For a new or materially changed responsive/stateful design family, use `ai/UI_CONSTRAINT_MODEL.md` as the implementation-contract vocabulary. Implement the smallest constraint system that explains the approved samples. If production needs geometry or adaptive behavior that cannot be derived from approved authority, report a specification `GAP` rather than inventing it.

## Procedure
1. Fresh-read the approved Figma state and current production implementation. Confirm the exact screen/state/viewport and canonical assets.
2. Inventory existing semantic structure and behavior, including the applicable state model rather than only the happy path: default/success plus loading, empty/no-result, partial, error/recovery, offline, disabled/busy, focus, and domain states where they can occur. Preserve semantics, accessibility, and business logic unless a structural change is approved.
3. Translate approved visual relationships and action hierarchy into the smallest responsive production constraint model. Treat Figma geometry as reference, not automatic CSS/code. Distinguish semantic, layout, and interaction/focus trees; classify visual/layout/text-flow/clip/interaction/focus/safe-content boxes; declare logical anchors, size behavior, constraint strength, elasticity ownership, text flow, and adaptive transforms. Treat available size, safe/system insets, text scale, locale/layout direction, platform/input mode, window configuration, accessibility preferences, and real product state as environment inputs only where they materially apply. Breakpoints describe available environment, not device names.
4. Perform a bounded cascade/style-resolution audit for the affected surface before adding overrides: relevant selectors/rules, specificity/order, inherited/custom properties, media queries, state classes, inline styles, and existing responsive behavior.
5. Implement the smallest production delta using existing semantic tokens/components/layout primitives where practical. Do not silently introduce off-system values or a generic framework/model aesthetic; repeated new values should express an explicit product decision across typography, colour, spacing/density, or surface/finish. Generated design-to-code output is not authority merely because it looks convenient.
6. Build/run the repository-required runtime. Verify functional behavior, then inspect actual runtime layout/computed styles at the approved state/viewport.
7. Compare meaningful relationships: anchors, dimensions, spacing, typography, wrapping, overflow/scroll, supported themes, safe-content behavior, semantic/focus order, and responsive changes in scope. Prefer invariant assertions over screenshot-only comparison. When responsive behavior changes, exercise a bounded falsification matrix across representative widths/heights and transform boundaries plus relevant text-scale, localization/RTL, state, input-mode, theme, and accessibility cases that can actually change the surface.
8. Exercise applicable interaction states. Verify recovery paths, appropriate loading/busy feedback, purposeful empty/no-result guidance, visible/logical focus, usable touch targets, non-hover-only primary actions, and non-color-only state meaning.
9. Diagnose mismatch from evidence—authority, structural model, cascade, intrinsic sizing, viewport/safe-area behavior, font/rendering, or state—and fix the cause rather than stacking screenshot-specific overrides.
10. Verify simulator/emulator and physical device only where current project rules or platform behavior require them; never upgrade emulation into physical evidence.
11. Before merge/release readiness, run a bounded severity-ranked UX review of the changed surface: intent/hierarchy, state completeness, affordance/feedback, recovery/destructive safety, copy, accessibility/focus/touch behavior, responsive behavior, and design-system drift. Resolve in-scope blockers without silently expanding scope.
12. Obtain owner visual acceptance where owner judgement is the acceptance boundary. Report `PASS`, `PARTIAL`, or `FAIL`; missing required runtime/device/owner evidence remains explicit.

## Fail-closed boundaries
`VISUAL APPROVED ≠ IMPLEMENTATION READY`. Before materially new design families, establish structural relationships such as regions/layers, scroll ownership, fixed vs elastic areas, shared axes/anchors, state changes, visible vs hit-target geometry, and responsive behavior.

Do not redesign approved Figma silently to make implementation easier. Do not replace an existing semantic production structure solely for visual convenience. Promote repeated geometry into shared constraints/tests only when it reduces repeated ambiguity; the solution must not become larger than the problem.

This skill does not authorize production mutation or release; current project rules and verification/release boundaries still govern them.

## Required outcome
Production preserves approved visual intent and existing semantics, actual runtime evidence explains what renders, required device/owner evidence is explicit, and any remaining mismatch has a bounded cause and next action.
