# U-GAS Agent Entry Point

Read this file before repository inspection, mutation, resume, or handoff work.

## Operating invariant

`READ CURRENT REPO -> VALIDATE TARGET -> TARGETED CHANGE -> WRITE/COMMIT -> FETCH AGAIN -> VERIFY`

Treat the current repository and its authoritative remote branch as the source of truth. Preserve uncommitted, unpushed, and unique local work. Never reset, clean, overwrite, force-push, or delete work merely to make a clone look current.

## Bootstrap and routing

1. Identify the exact repository and authoritative working branch from current repository metadata and local rules.
2. Read this repository's root PICA files and inspect the target's current status before changing anything.
3. For repository work, use the relevant guidance in `ai/GOVERNANCE.md`, `ai/GITHUB_WORKFLOW.md`, and `ai/REPOSITORY_STRUCTURE.md`.
4. For resume or handoff work, read `ai/SESSION_CONTINUITY.md` and the target's `CURRENT_STATE.md` completely.
5. For large, truncated, append-only, or structured files, use `ai/LARGE_FILE_PATCHING.md`.
6. Read only the procedures relevant to the task; do not load every document mechanically.
7. Make the smallest authorized change, verify it, commit when appropriate, and re-fetch the remote before claiming durable completion.

## Decision route

| Task signal | Route |
|---|---|
| Repository inspection, edit, or GitHub write | `ai/GOVERNANCE.md` + `ai/GITHUB_WORKFLOW.md` |
| Resume, continue, handoff, or where we stopped | `ai/SESSION_CONTINUITY.md` + `skills/u-gas-resume/SKILL.md` |
| Large, truncated, append-only, or structured file | `ai/LARGE_FILE_PATCHING.md` + `skills/u-gas-safe-patch/SKILL.md` |
| Verify a completed change or PASS claim | `skills/u-gas-verify-change/SKILL.md` |
| External repository or web research | `skills/u-gas-external-research/SKILL.md` |
| Overlapping or multi-agent work | `ai/MULTI_AGENT_COLLABORATION.md` |
| Non-trivial accepted behavior change | `ai/REPOSITORY_STRUCTURE.md` change-spec guidance |
| U-GAS self-check, PICA, route, or public-contract compliance | `ai/COMPLIANCE.md` + `scripts/check_u_gas.py` |
| Reviewing a new/external skill or durable capability | `skills/u-gas-skill-review/SKILL.md` |

Use the smallest relevant route. The normal sequence remains:

`READ CURRENT REPO -> VALIDATE TARGET -> TARGETED CHANGE -> WRITE/COMMIT -> FETCH AGAIN -> VERIFY`

## Active-session context

- Recent explicit owner intent remains valid working context until contradicted.
- Repository and Git authority win for repository facts.
- Durable continuity complements the current conversation; it does not erase it.
- A newer compatible owner decision must not be discarded merely because it is not yet persisted.
- Bootstrap is required when current repository truth, mutation, resume, handoff, or evidence is needed, not for every trivial follow-up.

## Authority and owner abstraction

Instruction precedence is: system/runtime safety and user intent, current target-repository rules, current repository/Git state, durable PICA continuity, then conversation memory or external research. The repository remains authoritative for repository facts. The user states the desired result; the agent handles routine technical mechanics and reports the smallest genuine human boundary.

Use a hybrid route: an existing remote project uses its verified canonical clone; a genuinely new project may begin local-first only when no remote exists and a safe persistent execution path is available. Exported or downloaded artifacts and session-sandbox files are not automatically a durable persistent project.

Do not add infrastructure without evidence of a recurring problem and a simpler-path failure. Completion means the intended write occurred, the actual state and required evidence were verified, and any human/device/manual boundary is explicit; write success alone is not completion.

## PICA contract

Every U-GAS-managed project exposes root `AGENTS.md`, `CURRENT_STATE.md`, `PROGRESS.md`, and `IDEAS.md`. Missing controls may be created as truthful minimal placeholders. Do not overwrite substantive controls or invent product scope, progress, state, ideas, credentials, or validation claims.

## Human boundaries

Handle routine technical work when safely possible. Stop for authentication, secrets, product judgement, destructive or irreversible actions, legal/security decisions, physical devices, or unclear authority. Never request passwords, tokens, recovery codes, private keys, or other secrets in chat.

## Purpose guard

Repository names and file presence do not establish product purpose. If current authoritative material is insufficient, classify the purpose as `PURPOSE UNKNOWN`, perform only neutral safe maintenance, and ask the smallest product-level question needed.
