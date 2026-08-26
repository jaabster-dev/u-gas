# Repository-backed long handoffs

Compact one-copy handoffs remain the normal path when the complete payload is short and reliable to transfer directly. Use this optional adapter proactively when a payload is long or materially structured, exact loss would be consequential, it already exists as durable structured material, or a previous clipboard/attachment transfer failed or became inaccessible. Do not use it as a character-count ritual for ordinary short prompts.

## Contract

Each pending handoff is one Markdown file at `handoffs/pending/<handoff-id>.md` with:

- `id`, `status: PENDING`, `created`, `target_repository`, and `target_branch` metadata;
- non-empty `Objective`, `Execution instructions`, `Constraints`, `Required verification`, and `Completion / consumption rule` sections.

Validate the directory without executing payloads:

```text
python3 scripts/check_handoff.py
```

Use `--target owner/repo` only for an optional exact-target assertion. Without it, any syntactically valid `owner/repo` declared by the payload is accepted. The payload is transport context, not repository authority; current repository state and owner intent still win.

Only `PENDING` is executable. After verified durable completion, remove the payload so an old launcher fails closed; Git history preserves provenance. If blocked, leave it pending and record the boundary through the repository's normal continuity surface. This adapter has no auto-executor, daemon, orchestration, arbitrary remote execution, secret storage, or manual user file-transfer ritual.
