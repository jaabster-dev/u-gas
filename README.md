# U-GAS

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE) [![Experimental](https://img.shields.io/badge/status-experimental-orange.svg)](#status-and-feedback) [![Tested with ChatGPT · Codex](https://img.shields.io/badge/tested%20with-ChatGPT%20%C2%B7%20Codex-blueviolet.svg)](#status-and-feedback)

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

## Start here

**[OPEN PROJECT STARTER →](https://jaabster-dev.github.io/u-gas/starter/)**

Use the runnable Starter first. Describe what you want to make, leave **My computer**
selected, copy the generated prompt, and paste it into ChatGPT or another coordinating AI.
If it gives you a Codex handoff, copy the whole marked block into Codex; then copy Codex's
clearly marked result back to ChatGPT and continue.

### Use U-GAS first: the action-first path

You can use U-GAS without learning its terminology first:

1. Describe what you want to make.
2. Choose where the project should live.
3. Copy the generated prompt.
4. Paste it into your coordinating AI chat.
5. If that AI asks for local execution, copy its ready-made handoff into a suitable executor.
6. Copy the executor's complete result back into the coordinating AI chat.
7. Continue talking to the AI about the project.

## NEXT ACTION

**Copy the complete prompt into your coordinating AI chat.** The tested local-first
handoff names Codex as the first example when local execution is needed; another
compatible authorized executor may be used where available.

Coming back later? Open `GIVE THIS TO YOUR NEXT AI CHAT.txt`, copy all of it, and paste it
into a new compatible AI chat to continue.

Open the public [Project Starter](https://jaabster-dev.github.io/u-gas/starter/) to use this
flow. Leave **My computer** selected for the currently tested route. GitHub and My server /
cloud remain visible in the Starter as planned routes, but are disabled until each has
dedicated end-to-end validation.

For the currently tested local-first journey, open the U-GAS Project Starter, describe
what you want to make, choose where it should live, and copy its complete prompt into
ChatGPT. ChatGPT is primarily the planning and coordination conversation: it should use
its own safe capabilities first. If the work requires persistent/local execution that
ChatGPT cannot access, it should discover the available capability and give you one
ready-to-copy handoff for Codex or another suitable local/coding executor. Paste that
handoff into the executor; it should create, change, and verify the real durable project
where indicated. Inspect the actual project/result, then return the executor's concise
report to ChatGPT so planning and reconciliation can continue there.

This keeps ordinary discussion in ChatGPT and invokes local/coding-agent execution only
when execution is needed. It may reduce unnecessary use of execution capacity, but U-GAS
makes no claim about credits, plans, entitlements, pricing, or guaranteed savings.

This exact local-first pattern has been owner-tested with ordinary ChatGPT and Codex on
macOS. Other tool combinations may work, but are not independently validated; you may
choose another compatible workflow that preserves the same capability boundaries and
user-controlled durable workspace.

The executor's response must include one complete concise return result and clearly tell
you: `Copy this complete result and paste it back into the AI chat that sent you here.`
Paste that result back into the coordinating chat so it can reconcile durable state and
continue. You should not have to decide which part of a technical report to copy.

## NEXT ACTION — after execution

**Copy this complete result and paste it back into the AI chat that sent you here.**
When the executor knows the exact file, project path, or verified browser URL, it should
name that target directly. You should not have to derive a localhost URL or interpret
routine command output.

### Resume after a pause or in a new AI chat

Open the durable project folder and open `GIVE THIS TO YOUR NEXT AI CHAT.txt`. Copy the
complete text into a new compatible AI chat. That stable human entry ticket points the AI
to the project's durable `AGENTS.md`, current U-GAS instructions, and actual PICA/project
state so it can reconstruct the current ACTIVE, NEXT, WAITING, and BLOCKED situation and
continue from the next useful action. It is not a fifth PICA file or a source of truth;
the durable project files remain authoritative. The artifact normally remains stable and
does not require special regeneration at every pause.

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

Before changing anything, read the current U-GAS README.md and AGENTS.md directly from
this public HTTPS source:
https://github.com/jaabster-dev/u-gas

Actually try to open and read that public URL before saying the U-GAS source is unavailable.
Use any safe read-only web, browser, or fetch method available to you. If one read method
is unavailable, discover or use another available read-only method when possible. A missing
GitHub connector, API access, authenticated integration, or local Git network is not proof
that this public URL cannot be read. Do not probe access with a write, dummy branch, commit,
file, or other mutation.

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
Also create or reconcile the separate stable human resume entry ticket
`GIVE THIS TO YOUR NEXT AI CHAT.txt`; it is not a fifth PICA/state authority. Begin that
file with a clear instruction to copy its complete text into a new AI chat to continue
the project. Its prompt must route through durable `AGENTS.md`, current U-GAS, and actual
PICA/project state, preserve existing work, and continue from the next useful action
without restarting.

If the public U-GAS source cannot be read after available read-only methods were attempted,
return exactly:
BLOCKED — U-GAS public source could not be read after available read-only methods were attempted: <specific reason>
If you cannot access a persistent filesystem, first perform safe capability discovery. If
an authorized persistent/local executor is available, prepare one complete copyable
handoff containing the project context, exact bounded objective, workspace authority,
constraints, verification requirements, and the instruction to return a concise result
to this conversation. Do not ask the user to invent the handoff or perform routine
Terminal/Git/file-transfer work. If no suitable capability exists, return exactly:
BLOCKED — persistent filesystem unavailable: <specific capability reason>
and include that one complete handoff whenever a suitable executor can be addressed.
Any executor handoff must require the executor's final response to contain one complete
concise return payload and the visible instruction: Copy this complete result and paste it
back into the AI chat that sent you here.
If you cannot access local Git, return exactly:
BLOCKED — local Git unavailable: <specific capability reason>
For another genuine human or capability boundary, return exactly:
BLOCKED — <specific boundary>
In every blocked case, do not simulate file creation or claim that anything was created or verified.

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

> [!TIP]
> Look for the real persistent project folder/path, the four files `AGENTS.md`,
> `CURRENT_STATE.md`, `PROGRESS.md`, and `IDEAS.md`, plus the agent's visible `PICA
> SELF-CHECK` with `READY` or a truthful `BLOCKED` result. If the agent only describes
> what it would do, skips actual folder/file evidence, or cannot show the path and files,
> the setup was not completed.

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

---

## Why U-GAS?

Decisions can get buried in chat. A different session may not know what happened, and
the owner becomes the memory, clipboard, and coordinator. U-GAS puts important project
state in inspectable files so capable agents can find the current path and continue.

### A typical workflow

**Plan → Persist → Execute → Verify → Resume**

You may not need U-GAS for a small project completed in one tool and one session. It is
most useful when work continues across sessions, tools, or repositories.

---

## How U-GAS works

### PICA: the four project controls

Every U-GAS-managed project exposes four visible files, in P-I-C-A order:

| File | Letter | Answers |
| --- | --- | --- |
| `PROGRESS.md` | P | What happened? |
| `IDEAS.md` | I | What might be useful later? |
| `CURRENT_STATE.md` | C | Where is the project now, and what comes next? |
| `AGENTS.md` | A | How should an AI agent work here? |

PICA is deliberately Markdown-first. It is not a database, installer, orchestration platform, or replacement for source control and CI. A repository-capable agent still reads current repository authority, preserves existing work, makes a bounded change, and verifies the result.

### Pause, resume, handoff, verify

To pause, record material state in `CURRENT_STATE.md` and useful evidence in `PROGRESS.md`. To resume, the agent reads current repository state first, reconciles it with PICA, verifies before acting, and follows the concrete `NEXT` action. Conversation memory is not a substitute for committed repository state.

Compact one-copy handoffs remain the default when the complete payload is short and reliable to transfer directly. Use the optional repository-backed [long-handoff transport](handoffs/README.md) proactively when a payload is long or materially structured, exact loss would be consequential, it already exists as durable structured material, or a previous clipboard/attachment transfer failed or became inaccessible. The transport validates `PENDING` payloads and removes them only after verified completion; it does not execute them.

For deeper procedures, see the [portable policies](ai/README.md), [self-check](scripts/check_u_gas.py), [handoff checker](scripts/check_handoff.py), and standard-library [tests](tests/).

---

## Limitations and safety

U-GAS does not:

- guarantee deterministic LLM behaviour or perfect memory;
- guarantee that a repository is safe merely because PICA files exist;
- choose product scope, grant credentials, approve destructive operations, or validate legal, account, security, device, or release decisions;
- replace source control, CI, security controls, or human judgement;
- claim reliability, adoption, benchmarks, industry-standard status, or independent validation.

If a run fails or feels confusing, record the repository and branch, expected action,
actual result, exact observable error, and whether files changed. Never include passwords,
tokens, recovery codes, private keys, or other secrets.

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

---

## Status and feedback

It is released under the [MIT License](LICENSE). For the first independent test, give
feedback by commenting on [Issue #1](https://github.com/jaabster-dev/u-gas/issues/1): where
you got stuck, what was unclear, what the agent failed to do, unexpected friction, and
whether the workflow resumed or worked as described. Do not post secrets or sensitive
private-repository content.

The distribution self-check verifies U-GAS's own files and routes. The optional `--project <path>` check verifies only readable, non-empty PICA files, the canonical upstream anchor in `AGENTS.md`, and the minimum `CURRENT_STATE.md` resume contract. These checks do not prove product correctness, current-state truth, runtime/model compliance, GitHub access, branch correctness, repository safety, or independent validation.
