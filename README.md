# U-GAS

U-GAS (Universal Agent System) is a small, Git-native operating model for AI-assisted work. It gives an agent a visible place to read current instructions, record what happened, resume safely, and park ideas without confusing them with accepted work.

> **EXPERIMENTAL / EARLY EXTERNAL TESTING** — U-GAS is not a proven industry standard. There is **NO INDEPENDENT USER VALIDATION YET**. It may reduce some context-loss, unsafe-mutation, stale-state, and handoff risks, but it does not guarantee deterministic LLM behaviour, prevent every instruction or memory failure, replace source control/CI/security controls, or remove the need for human, legal, account, or device decisions.

## Quick Start (about 5 minutes)

Use an existing GitHub repository that you control. Add these four files at its root, or ask an AI agent to add them after reading this repository's `AGENTS.md`:

```text
AGENTS.md          how the agent should work
CURRENT_STATE.md   where work is now and the next safe action
PROGRESS.md       what happened, with evidence
IDEAS.md          possibilities that are not accepted scope
```

Then start a new AI chat with this message, replacing the repository URL:

```text
I want to use U-GAS with my existing repository: <YOUR-REPOSITORY-URL>

Before changing anything, read the current U-GAS README and AGENTS.md directly from:
https://github.com/jaabster-dev/u-gas

Then inspect my repository's current branch, working tree, AGENTS.md, CURRENT_STATE.md,
PROGRESS.md, and IDEAS.md. Preserve existing work. Explain the smallest first action,
make the four-file control shell complete if it is missing, and stop when a real human
decision, authentication, secret, destructive action, device, or unclear product choice
is required.
```

Tell the agent in ordinary language what you want to accomplish. It should briefly restate the first useful result and ask for correction only when the product intent is genuinely unclear.

## The PICA model

PICA is the four-file project control contract:

- `AGENTS.md` — how an agent must inspect, change, verify, and hand off work.
- `CURRENT_STATE.md` — the compact resume surface: active work, next action, waiting state, and boundaries.
- `PROGRESS.md` — chronological evidence of what actually happened.
- `IDEAS.md` — a parking lot for unaccepted possibilities; an idea is not a requirement or backlog item.

PICA is deliberately visible and Markdown-first. Empty responsibilities use truthful minimal placeholders; agents must not invent progress or state just to fill a file.

## Pause and resume safely

To pause, tell the agent to stop at the current safe checkpoint and record any material change in `CURRENT_STATE.md` (and evidence in `PROGRESS.md` when useful). To resume, ask it to read the current repository state first, reconcile it with PICA, verify before acting, and then follow the concrete `NEXT` action. A local conversation or model memory is not a substitute for committed repository state.

## What U-GAS does not do

U-GAS is a workflow and documentation contract, not an installer, orchestration platform, security product, or guarantee of agent quality. It does not choose your product scope, grant credentials, approve destructive operations, validate legal/compliance requirements, or claim that a repository is safe merely because PICA files exist.

## Failure and friction

If a run fails or feels confusing, report: the repository and branch, the action you expected, what the agent actually did, the exact error or observable result, and whether any files changed. Do not paste passwords, tokens, recovery codes, private keys, or other secrets. Small onboarding failures are useful external-testing evidence.

## Repository contents

- [`AGENTS.md`](AGENTS.md) — public U-GAS entry point.
- [`ai/`](ai/) — portable guidance for governance, GitHub workflow, continuity, structure, and safe large-file handling.
- [`examples/first-project/`](examples/first-project/) — minimal PICA example.

## Status and license

U-GAS is experimental and intended for early external testing. **LICENSE DECISION PENDING.** No license file is included until the owner chooses one.
