# Repository-backed long handoffs

Compact one-copy handoffs remain the normal path when the complete payload is short and reliable to transfer directly. Use this optional adapter proactively when a payload is long or materially structured, exact loss would be consequential, it already exists as durable structured material, or a previous clipboard/attachment transfer failed or became inaccessible. Do not use it as a character-count ritual for ordinary short prompts.

## Contract

Each pending handoff is one Markdown file at `handoffs/pending/<handoff-id>.md` with:

- `id`, `status: PENDING`, `created`, `target_repository`, and `target_branch` metadata;
- non-empty `Objective`, `Execution instructions`, `Constraints`, `Required verification`, and `Completion / consumption rule` sections.

Before execution, resolve the target repository independently and validate the exact pending directory with an exact target assertion. For this repository's own generic distribution checks, the assertion may intentionally be omitted.

```text
python3 scripts/check_handoff.py
python3 scripts/check_handoff.py --target owner/repo
```

Use `--target owner/repo` for the actual execution path; a mismatch fails closed. Without it, any syntactically valid `owner/repo` declared by the payload is accepted only as an intentionally generic, read-only syntax/contract check. `target_branch` must be an explicit safe branch name or the documented `resolve from current authority` rule. The payload is transport context, not repository authority; current repository state and owner intent still win.

The originating agent must validate the exact payload against its intended target before issuing a launcher, commit/push it, fetch/read back the authoritative file, and validate that exact read-back payload again. Use `python3 scripts/check_handoff.py --handoff-id <handoff-id> --target <owner/repo>`; only a passing exact check may produce a launcher, and it prints `HANDOFF_READY: <handoff-id> -> <owner/repo>`. If validation fails, fix the payload itself and do not expose a broken launcher or ask the owner to relay errors. Only `PENDING` is executable. After verified durable completion, remove the exact payload, re-fetch authoritative repository state, and verify that exact path is absent; only then is the handoff consumed. The checker cannot prove historical consumption from an already absent file. Git history preserves provenance. If blocked, leave it pending and record the boundary through the repository's normal continuity surface. This adapter has no auto-executor, daemon, orchestration, arbitrary remote execution, secret storage, or manual user file-transfer ritual.
