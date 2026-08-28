# U-GAS Resume

## Purpose

Resume an existing U-GAS-managed project from durable current authority rather than conversation memory.

## When to use

Use for continue/resume/“where did we stop?”, a new or replacement AI chat for an existing project, cross-agent handoff, return after a meaningful context gap, or stale/degraded predecessor recovery.

## When not to use

Do not use for a genuinely brand-new project with no durable continuity, or a trivial active-session follow-up that does not depend on changed repository or project state.

## Resume action vs project next

`RESUME ACTION` is bootstrap/reconciliation work; `PROJECT NEXT` is the concrete project operation afterward. The required order is:

`RESUME ACTION -> RECONCILE -> VERIFY -> PROJECT NEXT`

## Procedure

1. Read the current U-GAS entry/policy and target project's `AGENTS.md`.
2. Establish actual local date/time before interpreting today, yesterday, tomorrow, or next when stale relative wording could affect reconciliation.
3. Establish the actual durable workspace or repository authority and inspect its current state.
4. Read `CURRENT_STATE.md` completely as the compact resume surface when present.
5. Reconstruct `ACTIVE`, `WAITING/PAUSED`, the concrete `PROJECT NEXT`, material `AFTER` ordering, blockers/boundaries, open handoffs, and interrupt/return target.
6. Reconcile current durable facts, fresh compatible owner intent, returned executor or human evidence, and only relevant history. Repository/filesystem facts win for current repository facts; newer compatible explicit owner decisions remain live until contradicted or durably persisted.
7. Verify only the facts and evidence required for the next safe action.
8. Preserve waiting or paused state instead of inventing work.
9. Continue to `PROJECT NEXT` only after reconciliation and verification.

## Stale/degraded session boundary

If the current session cannot establish authority after bounded recovery or repeatedly loses recent facts, stop substantive work. Preserve the smallest material continuity through a safe execution-capable path, then require a successor to fresh-bootstrap from durable authority. The old conversation is supporting context, not authority.

## Durable checkpoint

Never claim “saved” merely because information exists in chat or model memory. A durable checkpoint requires an actual write and authoritative read-back.

## Required outcome

A fresh agent can state `ACTIVE`, `WAITING/PAUSED`, the exact `PROJECT NEXT`, material blockers/boundaries, handoffs, and the return point without asking the user to reconstruct project history.
