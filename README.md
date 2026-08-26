# U-GAS

> *The conversation can be temporary; the project state is not.*

U-GAS (Universal Grabbers Agent System) helps keep a long-running AI project from losing its place between chats and tools. It stores important project state in ordinary files so another capable agent can continue without asking you to rebuild the whole story by hand.

> **EXPERIMENTAL / EARLY TESTING:** Practical testing has mainly used ChatGPT and Codex; other tools are not independently validated, and there is **NO INDEPENDENT USER VALIDATION YET**.

**On this page:**

- [Quick Start](#quick-start)
- [Why U-GAS?](#why-u-gas)
- [How U-GAS works](#how-u-gas-works)
- [Limitations and safety](#limitations-and-safety)
- [Status and feedback](#status-and-feedback)

## Quick Start

### What you need

You need:

- an AI coding agent that can create and keep files on your computer;
- permission for the agent to create a project folder and edit its files.

You do not need to create a GitHub repository. The agent will check the local tools it
needs and tell you if something is missing. A plain chat with no persistent file access
cannot perform this workflow; a session sandbox, temporary directory, or download
location is not durable project storage.

### Start a new local project — recommended first test

Replace only the project description below, copy the whole block, and give it to your
AI coding agent. You do not need to understand the technical instructions inside it.

```text
I want to start a new local U-GAS project. The project name and purpose are:
<DESCRIBE THE PROJECT IN ORDINARY LANGUAGE>

Before changing anything, read the current U-GAS README.md and AGENTS.md directly from:
https://github.com/jaabster-dev/u-gas

Establish a safe normal persistent local workspace yourself. Do not use a session
sandbox, temporary directory, or download/export location as the project. Derive a safe
filesystem name from the requested project name, create the project folder, and
initialize local Git if needed. Do not create a GitHub repository, remote, account, or
other external side effect.

Read the current U-GAS AGENTS.md and the portable templates in templates/pica/. Create
only missing root PICA controls (AGENTS.md, CURRENT_STATE.md, PROGRESS.md, IDEAS.md) from
those current templates. Never overwrite substantive existing content. Record only
truthful minimal project state, make an initial local commit when appropriate, and
re-read the actual files and local repository state from disk after writing.

If you cannot access a persistent filesystem or local Git, return exactly:
BLOCKED — <specific capability reason>
and do not simulate file creation or claim that anything was created or verified.

Before claiming readiness, visibly report:

PICA SELF-CHECK
- AGENTS.md: PRESENT / CREATED / BLOCKED
- CURRENT_STATE.md: PRESENT / CREATED / BLOCKED
- PROGRESS.md: PRESENT / CREATED / BLOCKED
- IDEAS.md: PRESENT / CREATED / BLOCKED

Claim READY only after the persistent folder, all four readable files, and local Git
repository state are actually verified. Do not claim CREATED, UPDATED, or VERIFIED from
prose simulation. If authority, project purpose, or a real human decision is unresolved,
report the specific boundary instead.

The first useful result is the verified local project folder and its PICA controls. Ask
for correction only if the project purpose is genuinely unclear.
```

### How to tell if it worked

You should be able to identify the real persistent project folder/path, the four files
`AGENTS.md`, `CURRENT_STATE.md`, `PROGRESS.md`, and `IDEAS.md`, and the agent's visible
`PICA SELF-CHECK` with `READY` or a truthful `BLOCKED` result. If the agent only
describes what it would do, skips actual folder/file evidence, or cannot show the path
and files, the setup was not completed.

<details>
<summary>Already use GitHub?</summary>

An existing GitHub-backed project remains supported. Give the agent its repository URL
and ask it to inspect the current repository and branch, preserve existing work, integrate
only missing PICA controls from current templates, and verify after writing. The existing
GitHub-backed, branch, collaboration, and remote-verification workflows still apply.
GitHub is also an optional later publication/collaboration/durability upgrade for a local
project, but adding a remote must be an explicit publication step; U-GAS must not create
one silently.

</details>

For either route, a local-only project uses its persistent filesystem and local Git
history as authority. Remote fetch/push verification is not applicable until a remote
exists. For the first external test, give feedback by commenting on [Issue #1](https://github.com/jaabster-dev/u-gas/issues/1): where you got stuck, what was unclear, what the agent failed to do, unexpected friction, and whether the workflow actually resumed or worked as described. Do not post secrets, tokens, passwords, private keys, or sensitive private-repository content.

If the agent cannot safely create files, stop and report the specific capability limit.
Otherwise, it should own the routine file and Git mechanics.

## Why U-GAS?

Decisions can get buried in chat. A different session may not know what happened, and
the owner becomes the memory, clipboard, and coordinator. U-GAS puts important project
state in inspectable files so capable agents can find the current path and continue.

### A typical workflow

**Plan → Persist → Execute → Verify → Resume**

You may not need U-GAS for a small project completed in one tool and one session. It is
most useful when work continues across sessions, tools, or repositories.

## How U-GAS works

### PICA: the four project controls

Every U-GAS-managed project exposes four visible files, in P-I-C-A order:

- `PROGRESS.md` — P: what happened;
- `IDEAS.md` — I: things you may consider later;
- `CURRENT_STATE.md` — C: where the project is now and what comes next;
- `AGENTS.md` — A: how an AI agent should work in this project.

PICA is deliberately Markdown-first. It is not a database, installer, orchestration platform, or replacement for source control and CI. A repository-capable agent still reads current repository authority, preserves existing work, makes a bounded change, and verifies the result.

### Pause, resume, handoff, verify

To pause, record material state in `CURRENT_STATE.md` and useful evidence in `PROGRESS.md`. To resume, the agent reads current repository state first, reconciles it with PICA, verifies before acting, and follows the concrete `NEXT` action. Conversation memory is not a substitute for committed repository state.

Compact one-copy handoffs remain the default when the complete payload is short and reliable to transfer directly. Use the optional repository-backed [long-handoff transport](handoffs/README.md) proactively when a payload is long or materially structured, exact loss would be consequential, it already exists as durable structured material, or a previous clipboard/attachment transfer failed or became inaccessible. The transport validates `PENDING` payloads and removes them only after verified completion; it does not execute them.

For deeper procedures, see the [portable policies](ai/README.md), [self-check](scripts/check_u_gas.py), [handoff checker](scripts/check_handoff.py), and standard-library [tests](tests/).

## Limitations and safety

U-GAS does not:

- guarantee deterministic LLM behaviour or perfect memory;
- guarantee that a repository is safe merely because PICA files exist;
- choose product scope, grant credentials, approve destructive operations, or validate legal, account, security, device, or release decisions;
- replace source control, CI, security controls, or human judgement;
- claim reliability, adoption, benchmarks, industry-standard status, or independent validation.

If a run fails or feels confusing, record the repository and branch, expected action, actual result, exact observable error, and whether files changed. Never include passwords, tokens, recovery codes, private keys, or other secrets. Practical testing so far has primarily used ChatGPT and Codex; Claude, Cursor, Copilot, and other paths remain experimental where not independently validated.

## Repository contents

<details>
<summary>Show the repository map</summary>

- [`PROGRESS.md`](PROGRESS.md), [`IDEAS.md`](IDEAS.md), [`CURRENT_STATE.md`](CURRENT_STATE.md), [`AGENTS.md`](AGENTS.md) — the four-file project control surface, in P-I-C-A order.
- [`ai/`](ai/) — portable governance, GitHub workflow, continuity, structure, collaboration, and safe large-file guidance.
- [`skills/`](skills/) — progressive-disclosure resume, safe-patch, verification, external-research, and skill-review procedures.
- [`handoffs/README.md`](handoffs/README.md) — optional repository-backed long-handoff transport.
- [`templates/pica/`](templates/pica/) — truthful templates for missing controls.
- [`examples/first-project/`](examples/first-project/) — minimal PICA example.
- [`scripts/check_u_gas.py`](scripts/check_u_gas.py) — optional read-only U-GAS/project self-check.
- [`scripts/check_handoff.py`](scripts/check_handoff.py) — read-only pending-handoff contract checker.
- [`tests/`](tests/) and [`.github/workflows/u-gas-self-tests.yml`](.github/workflows/u-gas-self-tests.yml) — standard-library contracts and CI self-tests.

</details>

## Status and feedback

U-GAS is experimental and intended for early external testing. It is released under the [MIT License](LICENSE). For the first independent test, give feedback by commenting on [Issue #1](https://github.com/jaabster-dev/u-gas/issues/1): where you got stuck, what was unclear, what the agent failed to do, unexpected friction, and whether the workflow resumed or worked as described. Do not post secrets or sensitive private-repository content.

The distribution self-check verifies U-GAS's own files and routes. The optional `--project <path>` check verifies only readable, non-empty PICA files, the canonical upstream anchor in `AGENTS.md`, and the minimum `CURRENT_STATE.md` resume contract. These checks do not prove product correctness, current-state truth, runtime/model compliance, GitHub access, branch correctness, repository safety, or independent validation.
