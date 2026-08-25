# U-GAS

U-GAS (Universal Agent System) is a small, Git-native operating model for AI-assisted work. It gives an agent a visible place to read current instructions, record what happened, resume safely, and park ideas without confusing them with accepted work.

> **EXPERIMENTAL / VERY EARLY EXTERNAL TESTING** — U-GAS is a very new system created in approximately five days from one user's real AI-assisted project workflow. Practical use and testing so far have been primarily with ChatGPT and Codex; there is **NO INDEPENDENT USER VALIDATION YET**. Portability to other agent or tool environments is intended but has not been independently demonstrated. U-GAS may reduce some context-loss, unsafe-mutation, stale-state, and handoff risks, but it does not guarantee deterministic LLM behaviour, prevent every instruction or memory failure, replace source control/CI/security controls, or remove the need for human, legal, account, or device decisions.

## What you need

To try the current U-GAS Quick Start, you need:

- a GitHub repository you control, preferably a safe test or sandbox repository for a first run;
- an AI agent that can actually read and change files in that repository, either through a GitHub integration or connector or through a local Git clone;
- permission for the agent to create or update the four PICA files and, when doing real project work, the relevant project files.

You do not need a specific AI tool or a specific GitHub connector. U-GAS is intended to be tool- and model-neutral. Practical testing so far has been primarily with ChatGPT and Codex; Claude, Cursor, Copilot, or another agent may also be usable, but those paths are currently experimental and unvalidated. Any agent used must be able to read the public U-GAS instructions, inspect the target repository, preserve existing work, and make and verify the changes required by the task.

For the bootstrap prompt below, the agent must be able to read both the public U-GAS instructions at `https://github.com/jaabster-dev/u-gas` and the target repository. A plain chat session with no repository or file access cannot perform this workflow reliably. If your AI tool cannot access a Git repository at all, the current Quick Start is not the right test path yet.

## Quick Start (about 5 minutes)

Recommended path: use an existing GitHub repository that you control and ask a repository-capable AI agent to inspect it and bootstrap the four PICA files safely. You should not need to understand Git mechanics or construct the files manually when the agent can do this. Manual creation is an alternative if you prefer or if your tool cannot safely create files:

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

Before claiming readiness, visibly report:

PICA SELF-CHECK
- AGENTS.md: PRESENT / CREATED / BLOCKED
- CURRENT_STATE.md: PRESENT / CREATED / BLOCKED
- PROGRESS.md: PRESENT / CREATED / BLOCKED
- IDEAS.md: PRESENT / CREATED / BLOCKED

Claim READY only when all four files are present, readable, and safely initialized, with
no unresolved authority or repository-purpose problem. Otherwise report:
BLOCKED — <specific reason>
```

Tell the agent in ordinary language what you want to accomplish. It should briefly restate the first useful result and ask for correction only when the product intent is genuinely unclear.

For the first external test, give feedback by commenting on [Issue #1](https://github.com/jaabster-dev/u-gas/issues/1): where you got stuck, what was unclear, what the agent failed to do, unexpected friction, and whether the workflow actually resumed or worked as described. Do not open a new issue for this first-test feedback, and do not post secrets, tokens, passwords, private keys, or sensitive private-repository content.

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

U-GAS is experimental and intended for early external testing. It is released under the [MIT License](LICENSE).
