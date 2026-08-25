# U-GAS Safe Patch

Use for large, truncated, append-only, generated, or structured canonical files. Read `ai/LARGE_FILE_PATCHING.md` first.

Never perform `PARTIAL READ -> RECONSTRUCT WHOLE FILE -> OVERWRITE`. Identify the authoritative version, obtain complete content or use the existing repository patch mechanism, make the smallest targeted change, check idempotency and bounded diff, then re-fetch and verify. If no safe complete-file path exists, report `BLOCKED`.
