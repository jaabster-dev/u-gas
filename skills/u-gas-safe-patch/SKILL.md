# U-GAS Safe Patch

## Purpose

Safely change large, truncated, append-only, generated, history-like, or structured canonical files without reconstructing unknown content.

## When to use

Use when connector output is truncated, the full target cannot be proven complete, the file is append-only/history-like or generated/structured, or the repository provides a targeted patch/update mechanism.

## When not to use

Do not use for a fully read, small, validated normal text file where ordinary bounded replacement is safe.

## Procedure

1. Read `ai/LARGE_FILE_PATCHING.md` and target-local rules.
2. Identify the authoritative target version and current state.
3. Inspect whether the repository already provides a targeted patch workflow, helper, or schema.
4. Reuse the existing mechanism instead of inventing parallel machinery.
5. Define the smallest intended transformation.
6. Obtain complete content, or apply a bounded targeted mutation without reconstructing unknown content.
7. Check idempotency and duplicate-insertion risk where applicable.
8. Inspect the bounded diff and changed filenames.
9. Verify generated or temporary patch-request cleanup when the mechanism requires it.
10. Re-fetch or re-read the authoritative result after mutation.

## Hard boundaries / Invariants

`PARTIAL READ -> RECONSTRUCT WHOLE FILE -> OVERWRITE` is forbidden. If no safe complete-content or targeted-mutation route exists, fail closed as `BLOCKED` rather than guessing or rebuilding.

## Required outcome

The exact intended target changed, adjacent unknown content was preserved, and final authoritative read-back verified the result.
