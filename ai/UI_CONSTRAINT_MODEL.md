# U-GAS UI Constraint Model

## Purpose

Define the smallest machine-readable mental model needed to translate approved product design into deterministic responsive UI without turning screenshots or per-viewport coordinates into implementation authority.

This is a semantic constraint contract, not a house style, framework, renderer, or requirement to serialize every pixel. Use it for repeated, responsive, stateful, accessibility-sensitive, or otherwise ambiguity-prone UI where relational authority reduces implementation drift.

Core invariant:

`DESIGN INTENT + ENVIRONMENT + CONSTRAINTS -> SOLVED LAYOUT -> RUNTIME PROOF`

Coordinates are solved output. They are not primary authority unless the product decision is explicitly absolute.

## Authority layers

Keep these layers distinct:

1. **Product semantics** — user task, information/action hierarchy, component identity, state meaning, reading/focus order.
2. **Design language** — typography, colour, spacing, density, radius, surface, iconography, motion, canonical assets.
3. **Relational layout** — regions, groups, boxes, anchors, intrinsic/min/max sizing, elasticity, text flow, scrolling, safe-area behavior, adaptive transforms.
4. **Environment** — available width/height, safe/system insets, density/scale, font/text scale, locale, layout direction, platform, input modality, window posture/configuration, accessibility preferences.
5. **Solved geometry** — actual positions and sizes for one concrete environment/state.
6. **Verification** — assertions over relationships, state/environment matrices, rendered evidence, device evidence, owner visual acceptance.

Do not collapse a higher layer into a lower one. A screenshot is evidence of one solved geometry, not the full relational model.

## Three trees

A responsive surface may have three related but non-identical trees:

- **Semantic tree** — meaning and logical ownership.
- **Layout tree** — containment and geometry.
- **Interaction/focus tree** — reachable controls and navigation order.

A responsive reflow may change the layout tree without silently changing semantic meaning or focus order. If visual order and interaction/reading order diverge materially, make the divergence explicit and verify accessibility.

## Required model vocabulary

### Identity and role

Every modeled object has stable identity and semantic role across environments unless an explicit transform replaces it.

Examples: `screen`, `header`, `navigation`, `workspace`, `pane`, `group`, `field`, `result-row`, `primary-action`, `status`, `footer`.

Repeated identity implies reuse of the same component/internal rules by default. A different position is not a different component.

### Box semantics

Do not treat every rectangle as equivalent. Classify relevant geometry as one or more of:

- `visual` — painted/visible content;
- `layout` — box participating in placement/sizing;
- `text-flow` — width/height governing line layout;
- `clip` — mask/overflow boundary;
- `interaction` — pointer/touch target;
- `focus` — focus indicator/navigation geometry;
- `safe-content` — region where critical content must remain unobscured.

A 24-unit icon may legitimately have a larger interaction/focus box. This is not visual-size drift.

### Size behavior

Each relevant axis uses one declared behavior:

- `fixed`
- `intrinsic`
- `fill`
- `elastic`
- `clamped(min,max)`
- `wrap`
- `scroll`
- `aspect-ratio`
- `transform-switched`

Exactly which region owns surplus/deficit space must be knowable. Do not distribute viewport delta across unrelated objects by accident.

### Anchors and relationships

Prefer logical relations over absolute coordinates:

- `leading/trailing/top/bottom`
- `centerX/centerY`
- `baseline`
- `same-axis`
- `gap`
- `inside/padding`
- `before/after`
- `aligned-with`
- `attached-to`

Use logical `leading/trailing` instead of physical `left/right` when the relation follows reading direction. Physical direction remains valid when the product meaning is genuinely physical.

### Constraint strength

When constraints can conflict, classify their strength:

- `REQUIRED` — violating it makes the model invalid.
- `STRONG` — preserve unless a declared transform or environmental necessity overrides it.
- `PREFERRED` — desired presentation that may yield to stronger constraints.
- `FALLBACK` — behavior activated when stronger presentation cannot fit.

Do not resolve conflicts through unrecorded optical nudges.

### Adaptive transforms

A change in available environment may apply an explicit transform:

- `PRESERVE`
- `RESIZE`
- `REFLOW`
- `REPOSITION`
- `REVEAL`
- `HIDE`
- `REPLACE`
- `STACK`
- `SPLIT`
- `SCROLL`
- `PRESENTATION_CHANGE`

Transforms apply at component/pane level where possible. Do not duplicate whole screens merely because width changes.

Breakpoints are consequences of content/interaction needs and supported environment classes, not device names. `iPad` or `Android tablet` is not a sufficient layout rule.

### Text as geometry

Text is a first-class layout input. Relevant text authority includes:

- semantic role/style token;
- content;
- font metrics;
- intrinsic width;
- declared flow width;
- wrap policy;
- min/max lines where intentional;
- truncation policy;
- baseline;
- text/font scaling behavior;
- localization expansion behavior.

Line count and text height are solved outputs. Fixed text boxes that depend on one string or one font scale are suspect unless explicitly required.

### Environment inputs

Model the inputs that can materially alter layout:

```text
Environment {
  availableWidth
  availableHeight
  safeInsets
  densityOrScale
  textScale
  locale
  layoutDirection
  platform
  inputModality
  windowPosture
  accessibilityPreferences
}
```

Only include an input in a product specification when it can affect that product. The vocabulary is comprehensive; each product model stays minimal.

Safe/system insets distinguish edge-to-edge visual canvas from safe critical content. Backgrounds may extend beyond safe-content bounds while important content/controls remain inset.

### State inputs

Layout can depend on real product state: loading, empty, no-result, partial, error, offline, busy, disabled, selected, expanded, focus, validation, permission, or domain-specific state.

State-driven geometry change must be attributable to a declared state/variant, not accidental CSS/runtime drift.

## Canonical reasoning order

For a new or materially changed responsive family, reason in this order:

`INTENT -> IDENTITY -> SEMANTIC ROLE -> GROUP -> TREES -> BOX SEMANTICS -> ANCHORS -> SIZE BEHAVIOR -> CONSTRAINT STRENGTH -> ELASTICITY -> TEXT FLOW -> ENVIRONMENT -> ADAPTIVE TRANSFORM -> SOLVED PLACEMENT`

If a later step exposes a contradiction, return to the earliest incorrect authority instead of patching the final coordinates.

## Compact grammar

A product may encode the model in its existing specification format. The semantics below are normative; YAML is illustrative, not a mandated storage technology.

```yaml
component: InputGroup
role: primary-input
children: [LabelRow, Input, TrailingAction]

layout:
  axis: vertical
  size:
    inline: fill
    block: intrinsic
  gap: space.8

constraints:
  - LabelRow.leading == Input.leading @ REQUIRED
  - LabelRow.trailing == Input.trailing @ REQUIRED
  - TrailingAction.trailing == Input.trailing - space.12 @ REQUIRED
  - TrailingAction.centerY == Input.centerY @ REQUIRED

boxes:
  TrailingAction.visual: 24x24
  TrailingAction.interaction:
    min: platform.minimumTouchTarget

text:
  Label:
    width: intrinsic
  Value:
    width: fill
    wrap: allowed
    lines: dynamic

adapt:
  compact->medium:
    InputGroup: PRESERVE
    Input.inline: RESIZE
    constraints: PRESERVE

states:
  error:
    add: ErrorText
    after: Input
    groupBlockSize: intrinsic
```

The implementation may use CSS Grid/Flexbox, SwiftUI, Auto Layout, Compose, or another renderer. Renderer choice must preserve the same semantic constraints rather than becoming a second design authority.

## Solver obligations

Given a supported environment/state, an implementation must be able to answer:

1. Which identities exist?
2. Which semantic/layout/interaction parent owns each identity?
3. Which dimensions are invariant, intrinsic, elastic, clamped, wrapped, scrolled, or transformed?
4. Which object owns positive/negative space on each relevant axis?
5. Which anchors determine each meaningful placement?
6. Which constraints may yield, and in what order?
7. Which text-flow width determines wrapping?
8. Which safe/system insets affect visual versus critical content?
9. Which adaptive transform is active?
10. Which reading/focus order remains valid after reflow?

If the answer depends on inventing a coordinate not derivable from authority, report a specification `GAP`.

## Verification model

Prefer invariant assertions over screenshot-only comparison. Examples:

```text
TrailingAction.trailing == Input.trailing - space.12
TrailingAction.centerY == Input.centerY
ResultRow.internalPadding == token.rowPadding
ResultRow.visualIcon == token.iconSize
ResultRow.interactionTarget >= platform.minimumTouchTarget
Header.role == header across supported widths
unexpectedOverlap == false
unexpectedOverflow == false
focusOrder preserves semantic task order
```

Test a bounded matrix appropriate to the changed surface:

- representative minimum/nominal/maximum supported widths and heights;
- each declared adaptive-transform boundary plus at least one value on either side;
- relevant text-scale extremes;
- longest/representative localized content and RTL when localization applies;
- applicable interaction/error/loading/empty states;
- relevant input modes when keyboard/pointer behavior matters;
- Light/Dark and accessibility preferences when they affect presentation.

Do not multiply the matrix mechanically. Select cases that can falsify the declared invariants.

A screenshot/render remains necessary for visual character and optical quality, but it cannot prove relational correctness by itself.

## Platform constraints versus product decisions

Platform guidance is an input, not a copied house style.

Examples:
- respect platform safe/system insets;
- support platform text scaling and accessibility preferences;
- satisfy platform interaction-target and focus expectations;
- preserve standard gesture/input alternatives;
- adapt to resizable windows rather than assuming a device model.

Do not import another system's colour palette, spacing grid, breakpoints, component appearance, or navigation pattern unless the product explicitly adopts it.

## Figma relationship

Figma is design authority and a source of evidence for identity, component reuse, Auto Layout/constraints, visual geometry, typography, tokens, and approved compositions.

One Figma frame is one solved sample. Multiple approved frames/states are observations the relational model must explain. Do not implement independent coordinate sets for each frame when one constraint model can explain them.

When Figma metadata is insufficient to distinguish two plausible relational models, surface the ambiguity for owner/product decision. Do not infer a hidden rule from visual coincidence.

## Promotion gate

For a materially new responsive family:

`VISUAL APPROVED != STRUCTURAL MODEL APPROVED != IMPLEMENTATION VERIFIED`

Implementation-ready requires:
- approved visual intent;
- sufficient semantic/constraint authority to solve supported environments without local invention;
- declared unresolved gaps = none for in-scope behavior;
- a verification matrix capable of falsifying the important invariants.

Existing proven surfaces are not retroactively blocked merely because this model was introduced. Apply it when new responsive work, a demonstrated defect, shared primitive risk, or explicit owner decision makes relational authority material.

## Anti-patterns

Reject:
- screenshot tracing as responsive implementation;
- per-breakpoint magic coordinates that restate solved geometry;
- device-name-only layouts;
- hidden `left/right` assumptions for logical reading-order relations;
- visual boxes used as touch/focus authority without classification;
- fixed text heights derived from one language/font scale;
- CSS/renderer quirks promoted into design authority;
- duplicate components that differ only because their parent changed;
- unexplained cross-axis movement;
- compensating offsets that leave the wrong generic mechanism active;
- exhaustive serialization that is larger than the ambiguity it prevents.

The objective is not maximal specification. It is the **smallest constraint system that uniquely explains the intended product behavior and can be tested at runtime**.
