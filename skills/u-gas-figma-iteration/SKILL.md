# U-GAS Figma Iteration

## Purpose
Run a bounded, reviewable iteration loop on an existing Figma design while preserving candidate history and separating write/structure evidence from visual success.

## When to use
Use when an owner and agent inspect, edit, compare, or version reviewable candidates in an existing Figma file or board and current project authority establishes Figma as the design surface.

## When not to use
Do not use for one-off image generation, non-Figma discussion, simple read-only inspection, production implementation, or automatic design promotion.

## Authority
Current project rules establish the authoritative design file and any approved/reusable components. Current Figma state is authority for node identity, structure, and placement; stale IDs must be revalidated. Owner visual approval remains authority for intended visual outcome.

## Constraint-model routing
For a new or materially changed responsive/stateful design family, use `ai/UI_CONSTRAINT_MODEL.md`. Formalize only relationships whose ambiguity can change implementation. Treat each Figma frame as a solved sample, not the complete responsive specification; missing relational authority is a `GAP`, not permission to invent coordinates.

## Procedure
1. Identify and fresh-read the current candidate, parent/board, state, and geometry relevant to the requested delta. Resolve stale identity before write.
2. Before creating reusable product UI, perform a bounded authority-discovery pass. Reuse/clone/adapt approved authority when it exists; if required authority is missing or ambiguous, stop before write rather than fabricate a lookalike.
3. Apply one bounded delta as a new candidate. Preserve the prior candidate unless cleanup is authorized; never call an in-place mutation a new version.
4. Give the candidate a unique identity and explicit review state. Distinguish created work from planned/not-drawn work.
5. For interactive or reusable screen-family changes, run a bounded product-intent/completeness preflight: identify the primary task, action hierarchy, and costliest plausible mistake; cover applicable non-happy-path states (loading, empty/no-result, partial, error/recovery, offline, disabled/busy, focus, and domain states); keep primary actions touch-reachable without hover; require visible focus, non-color-only state cues, and proportionate destructive safeguards. Prefer undo/recovery for safely reversible actions and stronger confirmation only for genuinely irreversible ones. Do not invent states that cannot occur.
6. Run only relevant geometry/text preflight. Resolve compared nodes into a common coordinate space including ancestor transforms; do not treat raw local bounds as resolved geometry. Classify overflow by intended scroll axis before calling it failure. For text-dependent layout, verify actual typography/box/wrapping and fresh-read post-layout geometry.
7. Establish the smallest relational model needed by the delta: stable identity/role, semantic groups, semantic/layout/interaction-focus trees, visual/layout/text-flow/clip/interaction/focus/safe-content box semantics, logical anchors, fixed/intrinsic/elastic/clamped/wrap/scroll size behavior, constraint strength, elasticity ownership, text flow, applicable environment inputs, and explicit adaptive transforms. Prefer logical leading/trailing for reading-direction relations. A width/height change must propagate through declared dependencies; unexplained cross-axis movement or per-device coordinate duplication is a model gap.
8. Preserve current design-system and visual-character authority. Reuse existing tokens/components before adding values. Where a genuinely new family requires a decision, make the minimum explicit choice across typography, colour, spacing/density, and surface/finish rather than falling back to framework/model defaults.
9. Reuse canonical/native/library assets exactly where they are authority; do not redraw an approved asset and call it equivalent.
10. Fresh-read metadata/structure after write and verify node, parent/sibling relationship, state/text/geometry, and visibility.
11. Inspect the actual post-write screenshot/render. Keep evidence distinct: `WRITE PASS` means mutation accepted; `STRUCTURE PASS` means fresh structure matches; `VISUAL PASS` means a fresh render satisfies the requested visible condition. `WRITE ≠ STRUCTURE ≠ VISUAL`.
12. Before promotion of a materially changed interactive surface, run a bounded severity-ranked UX review covering hierarchy, state gaps, affordance/feedback, recovery, copy, accessibility/focus/touch behavior, and design-system drift. Keep unrelated findings out of the accepted delta.
13. Return `PASS`, `PARTIAL`, or `FAIL` and preserve the exact unresolved boundary. Promote a review candidate only after required checks and owner visual approval.

## Fail-closed boundaries
Do not infer visual correctness from API/write success, coordinates, metadata, or nominal dimensions. If identity, canonical authority, common coordinate space, actual render, or required owner approval is unavailable or ambiguous, preserve the current authority and report the result as partial/unverified rather than correcting from inference.

This skill does not authorize Figma access or mutation; current project/tool authorization still governs execution.

## Required outcome
A competent agent can identify the source and candidate, state the requested delta, distinguish write/structure/visual evidence, explain any unresolved geometry or authority boundary, and hand a reviewable candidate to the owner without silently overwriting approved authority.
