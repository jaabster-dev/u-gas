# U-GAS Large-File Safety

Use this procedure for truncated or partial content, large or append-only files, structured canonical data, generated files, whole-file update APIs, or any edit where unseen bytes could be harmed.

## Safe-edit procedure

Never perform `PARTIAL READ -> RECONSTRUCT WHOLE FILE -> OVERWRITE`. Use `READ CURRENT -> VALIDATE TARGET -> TARGETED CHANGE -> WRITE -> FETCH AGAIN -> VERIFY`:

1. Identify the authoritative file/ref and current identity, version, or SHA. Obtain complete current content through the authorized interface where possible; for a claimed immutable blob, verify its beginning, target, and end against that identity.
2. Prefer an existing repository patch helper/workflow. If complete content plus an identity/version guard is available, make only the bounded edit and write with the guard where possible. With a complete persistent canonical clone, edit locally, inspect the diff, run required checks, and commit/push through the normal workflow.
3. For inserts or appends, use stable identity, detect duplicates, and fail closed rather than inserting twice. For replacements, verify the target is unique and current. Do not invent a universal patch schema.
4. Verify the expected file changed, unintended files did not, the diff is bounded, required tests and evidence pass, and authoritative content is re-read after the write. Remove temporary one-off patch infrastructure when the task is complete if repository rules allow.
5. If neither safe complete-content mutation nor a safe targeted mutation route exists, report `BLOCKED — safe complete-file mutation path unavailable`.

For small files, complete-read before update remains the minimum safety property: complete current content, current identity guard, and bounded diff.
