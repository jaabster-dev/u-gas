# U-GAS

> Chats fade into night<br>
> Project truth remains in files<br>
> Next hands find the path

> *The conversation can be temporary; the project state is not.*

U-GAS (Universal Grabbers Agent System) is a small, Git-native operating model for AI-assisted work. It gives a project an explicit place for current instructions, state, progress, ideas, handoffs, and verification so a later or different repository-capable agent can continue from evidence instead of reconstructing everything from chat memory.

> **EXPERIMENTAL / VERY EARLY EXTERNAL TESTING** — Practical testing has primarily been with ChatGPT and Codex. There is **NO INDEPENDENT USER VALIDATION YET**. U-GAS is intended to be portable to other agents and tools, but those paths remain experimental and unvalidated.

**Jump to:** [Quick Start](#quick-start) · [Why U-GAS?](#why-u-gas) · [How it works](#how-u-gas-works) · [Safety](#safety-and-limitations) · [Feedback / Status](#status-and-license)

## Why U-GAS?

Long-lived AI work often crosses chats, tools, repositories, and sessions. A useful decision can remain buried in a conversation; an execution agent may not see it; a later session may guess what happened; and the human becomes the memory, clipboard, Git/GitHub coordinator, and handoff mechanism.

U-GAS moves material project state into the repository that the work already depends on. It does not give an LLM perfect memory and it does not guarantee that an agent will follow instructions. It gives agents a shared, inspectable authority to reconcile against.

### A typical workflow

```mermaid
flowchart LR
    A[Plan] --> B[Persist]
    B --> C[Execute]
    C --> D[Verify & resume]
```

Different agents do not need to share hidden memory if they can read the same explicit project state, current repository rules, and verified Git history.

### Before and with U-GAS

| Without U-GAS | With U-GAS |
| --- | --- |
| Chat discussion → decision stays in conversation → execution agent lacks context or guesses → later session reconstructs state | Chat discussion → material state is persisted → execution agent reads current authority → change is implemented and verified |
| The owner repeats what happened and what comes next | The repository provides an explicit resume point |
| Handoffs depend on memory, copy/paste, and manual Git coordination | Handoffs can use current PICA, Git history, and an optional exact repository-backed payload |

U-GAS reduces coordination and reconstruction burden. It does not eliminate context loss, unsafe edits, stale state, or human decisions.

### Who is it for?

U-GAS is most relevant when you:

- work across fresh AI sessions or more than one AI tool/agent;
- separate conversational planning from repository execution;
- maintain a longer-lived project or multiple repositories;
- have experienced forgotten decisions, repeated work, stale assumptions, unsafe edits, or difficult resume/handoffs.

You may not need it for a small project completed in one tool and one session, with little continuity or handoff pain. The extra project structure should earn its cost.

## Quick Start

### What you need

For the recommended first test, you need:

- a file/repository-capable AI agent with real persistent local filesystem access;
- Git available locally where the agent can use it;
- permission for the agent to create and edit files in a normal persistent user workspace.

**NO GITHUB REPOSITORY IS REQUIRED for this first local-first path.** A plain chat with no
persistent file access cannot perform it, and a session sandbox, temporary directory, or
download location is not durable project storage.

You do not need a specific AI tool or connector. Practical testing so far has primarily
used ChatGPT and Codex; other agents may also be usable, but those paths remain
experimental and unvalidated.

### Start a new local project — recommended first test

Give the agent only the project name and purpose in ordinary language. Copy this complete
prompt:

<details>
<summary>Copy the complete local-first prompt</summary>

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

</details>

### Already have a GitHub repository?

An existing GitHub-backed project remains supported. Give the agent its repository URL
and ask it to inspect the current remote/branch/status, preserve existing work, integrate
only missing PICA controls from current templates, and verify after writing. The existing
canonical-clone, remote-authority, branch/PR, and collaboration workflows still apply.
GitHub is also an optional later publication/collaboration/durability upgrade for a local
project, but adding a remote must be an explicit publication step; U-GAS must not create
one silently.

For either route, a local-only project uses its persistent filesystem and local Git
history as authority. Remote fetch/push verification is not applicable until a remote
exists. For the first external test, give feedback by commenting on [Issue #1](https://github.com/jaabster-dev/u-gas/issues/1): where you got stuck, what was unclear, what the agent failed to do, unexpected friction, and whether the workflow actually resumed or worked as described. Do not post secrets, tokens, passwords, private keys, or sensitive private-repository content.

If the agent cannot safely create files, manual creation from the portable PICA templates is an alternative; preserve substantive existing project rules and state. Otherwise, the agent should own routine Git and file mechanics.

### What happens next

The agent should own routine Git and file mechanics. You should only need to decide product scope, provide unavailable credentials or environment access, or approve a genuinely consequential boundary.

If the target `AGENTS.md` is missing, the agent may initialize it from the template. If it already contains substantive project rules, those rules must be preserved and only the smallest U-GAS bootstrap anchor should be integrated. After the PICA shell is installed, future repository-capable sessions can start from the target repository's `AGENTS.md`, which points back to the current U-GAS authority. Tell the agent in ordinary language what you want to accomplish; it should ask for correction only when product intent is genuinely unclear.

## How U-GAS works

### PICA: the four project controls

Every U-GAS-managed project exposes four visible root controls, in P-I-C-A order:

- `PROGRESS.md` — P: chronological evidence of what actually happened;
- `IDEAS.md` — I: possibilities that are not accepted scope;
- `CURRENT_STATE.md` — C: the compact resume surface: active work, next action, waiting state, and boundaries;
- `AGENTS.md` — A: how an agent must inspect, change, verify, and hand off work.

PICA is deliberately Markdown-first. It is not a database, installer, orchestration platform, or replacement for source control and CI. A repository-capable agent still reads current repository authority, preserves existing work, makes a bounded change, and verifies the result.

### Pause, resume, handoff, verify

To pause, record material state in `CURRENT_STATE.md` and useful evidence in `PROGRESS.md`. To resume, the agent reads current repository state first, reconciles it with PICA, verifies before acting, and follows the concrete `NEXT` action. Conversation memory is not a substitute for committed repository state.

Compact one-copy handoffs remain the default when the complete payload is short and reliable to transfer directly. Use the optional repository-backed [long-handoff transport](handoffs/README.md) proactively when a payload is long or materially structured, exact loss would be consequential, it already exists as durable structured material, or a previous clipboard/attachment transfer failed or became inaccessible. The transport validates `PENDING` payloads and removes them only after verified completion; it does not execute them.

For deeper procedures, see the [portable policies](ai/README.md), [self-check](scripts/check_u_gas.py), [handoff checker](scripts/check_handoff.py), and standard-library [tests](tests/).

## Safety and limitations

U-GAS does not:

- guarantee deterministic LLM behaviour or perfect memory;
- guarantee that a repository is safe merely because PICA files exist;
- choose product scope, grant credentials, approve destructive operations, or validate legal, account, security, device, or release decisions;
- replace source control, CI, security controls, or human judgement;
- claim reliability, adoption, benchmarks, industry-standard status, or independent validation.

If a run fails or feels confusing, record the repository and branch, expected action, actual result, exact observable error, and whether files changed. Never include passwords, tokens, recovery codes, private keys, or other secrets. Practical testing so far has primarily used ChatGPT and Codex; Claude, Cursor, Copilot, and other paths remain experimental where not independently validated.

## Repository contents

- [`PROGRESS.md`](PROGRESS.md), [`IDEAS.md`](IDEAS.md), [`CURRENT_STATE.md`](CURRENT_STATE.md), [`AGENTS.md`](AGENTS.md) — the four-file project control surface, in P-I-C-A order.
- [`ai/`](ai/) — portable governance, GitHub workflow, continuity, structure, collaboration, and safe large-file guidance.
- [`skills/`](skills/) — progressive-disclosure resume, safe-patch, verification, external-research, and skill-review procedures.
- [`handoffs/README.md`](handoffs/README.md) — optional repository-backed long-handoff transport.
- [`templates/pica/`](templates/pica/) — truthful templates for missing controls.
- [`examples/first-project/`](examples/first-project/) — minimal PICA example.
- [`scripts/check_u_gas.py`](scripts/check_u_gas.py) — optional read-only U-GAS/project self-check.
- [`scripts/check_handoff.py`](scripts/check_handoff.py) — read-only pending-handoff contract checker.
- [`tests/`](tests/) and [`.github/workflows/u-gas-self-tests.yml`](.github/workflows/u-gas-self-tests.yml) — standard-library contracts and CI self-tests.

## Status and license

U-GAS is experimental and intended for early external testing. It is released under the [MIT License](LICENSE). For the first independent test, give feedback by commenting on [Issue #1](https://github.com/jaabster-dev/u-gas/issues/1): where you got stuck, what was unclear, what the agent failed to do, unexpected friction, and whether the workflow resumed or worked as described. Do not post secrets or sensitive private-repository content.

The distribution self-check verifies U-GAS's own files and routes. The optional `--project <path>` check verifies only readable, non-empty PICA files, the canonical upstream anchor in `AGENTS.md`, and the minimum `CURRENT_STATE.md` resume contract. These checks do not prove product correctness, current-state truth, runtime/model compliance, GitHub access, branch correctness, repository safety, or independent validation.
