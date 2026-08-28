# U-GAS Verify Change

## Purpose

Independently judge whether an implementation or change satisfies the accepted requirement.

## When to use

Use after implementation or an executor/Codex/Claude/human result, before accepting a PASS, milestone, or release-ready claim, or when asked whether a change was really completed.

## When not to use

Do not use as implementation itself, or where no requirement or acceptance boundary exists yet.

## Verification invariant

`REQUIREMENT -> ACTUAL DIFF/STATE -> REQUIRED TESTS -> REQUIRED EVIDENCE -> VERDICT`

## Procedure

1. Recover the exact accepted requirement and non-goals.
2. Inspect authoritative files and current state, not an implementation summary.
3. Inspect the actual diff/change scope and check for unintended adjacent changes or scope expansion.
4. Run or inspect repository-required tests and checks.
5. Distinguish evidence levels: source present; build/runtime ready; test executed; test passed; browser/runtime verified; physical-device/manual verified; and independent external validation where applicable.
6. Do not promote one evidence class into another, and compare any required external or manual evidence.
7. Return one truthful verdict: `PASS`, `FAIL`, or `NEEDS HUMAN VERIFICATION` (or another canonical U-GAS equivalent when policy requires it).
8. Preserve the unresolved boundary and exact next verification action.

## Hard boundaries / Invariants

An AI saying `PASS` is not itself proof. Where mechanically observable evidence exists, inspect the evidence/state itself and never invent missing evidence.

## Required outcome

A reader can tell what was required, what actually changed, what tests/evidence exist, what remains unverified, and why the verdict follows.
