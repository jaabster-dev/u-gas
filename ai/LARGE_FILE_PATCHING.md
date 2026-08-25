# U-GAS Large-File Safety

## Recognition

Use this procedure for truncated or partial content, large or append-only files, structured canonical data, generated files, update APIs that replace whole files, or any edit where unseen bytes could be harmed.

## Hard invariant

Never perform `PARTIAL READ -> RECONSTRUCT WHOLE FILE -> OVERWRITE`.

Use `READ CURRENT -> VALIDATE TARGET -> TARGETED CHANGE -> WRITE -> FETCH AGAIN -> VERIFY`.

## Portable safe-edit ladder

1. Identify the authoritative file/ref and current identity, version, or SHA when exposed.
2. Obtain complete current content through the authorized repository interface.
3. If complete content and an identity/version guard exist, make only the targeted edit, verify a bounded diff, write with the guard where possible, and re-fetch.
4. Reuse an existing repository patch helper/workflow when one exists; do not invent a parallel mechanism.
5. With a complete persistent local clone, edit the complete file locally, inspect the diff, run required checks, commit/push, and re-fetch.
6. Otherwise report `BLOCKED — safe complete-file mutation path unavailable`.

For inserts/appends, use stable identity where practical, detect duplicates, and fail closed rather than append twice. For replacements, verify the target is unique and current. A safe edit is incomplete until the expected file changed, unintended files did not, the diff is bounded, required evidence passes, and authoritative remote content is re-read.

## Complete-content ladder

Identify the authoritative file/ref and current identity, version, or SHA. Prefer immutable complete content by blob-SHA where exposed; when claiming a complete blob, verify its beginning, target, and end against that identity. If complete current content plus a current identity guard are truly available, make the bounded edit, write with the guard where possible, and re-fetch. Reuse an existing repository-side adapter rather than inventing a universal patch schema. A temporary branch/PR/diff review or complete persistent local clone is a safe route where appropriate. Only then report `BLOCKED — safe complete-file mutation path unavailable`.

For small files, complete-read before update. The minimum safety property is complete current content + current identity guard + bounded diff. Remove temporary one-off patch infrastructure when its task is complete if repository rules allow.
