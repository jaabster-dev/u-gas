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
6. Make the smallest authorized change, verify it, commit when appropriate, and re-fetch the remote before claiming durable completion.

## PICA contract

Every U-GAS-managed project exposes root `AGENTS.md`, `CURRENT_STATE.md`, `PROGRESS.md`, and `IDEAS.md`. Missing controls may be created as truthful minimal placeholders. Do not overwrite substantive controls or invent product scope, progress, state, ideas, credentials, or validation claims.

## Human boundaries

Handle routine technical work when safely possible. Stop for authentication, secrets, product judgement, destructive or irreversible actions, legal/security decisions, physical devices, or unclear authority. Never request passwords, tokens, recovery codes, private keys, or other secrets in chat.

## Purpose guard

Repository names and file presence do not establish product purpose. If current authoritative material is insufficient, classify the purpose as `PURPOSE UNKNOWN`, perform only neutral safe maintenance, and ask the smallest product-level question needed.
