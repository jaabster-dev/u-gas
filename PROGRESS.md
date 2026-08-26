# Progress

> Footprints wait in snow<br>
> Work will mark the path in time<br>
> History starts here

Add chronological evidence here when material work occurs; keep current resume state in `CURRENT_STATE.md`.

## 2026-08-25 — Operational core parity v0.1

Portable routing, governance, continuity, safe-edit, verification, collaboration, research, PICA-template, example, and Quick Start improvements were added for early external testing. No independent validation is claimed.

## 2026-08-25 — Portable parity v0.2

GAS-vs-U-GAS reconciliation added fuller portable governance, GitHub workflow, continuity, large-file safety, repository-structure, collaboration, AI-guidance, compliance, skills, read-only self-check, standard-library tests, CI self-test, and project-check coverage. `scripts/check_u_gas.py`, `python -m unittest -v` (13 tests), and the example project check passed. No independent validation is claimed.

## 2026-08-26 — Bounded project-contract hardening

The target-project checker now requires readable/non-empty PICA controls, an unconditional exact canonical U-GAS anchor in `AGENTS.md`, and either the truthful minimal `CURRENT_STATE.md` placeholder or a real four-responsibility resume surface. README/COMPLIANCE now distinguish local contract checks from claims they cannot prove. Local self-check, explicit A–E fixtures, and 18 standard-library tests passed; GitHub Actions self-test run `32898765684` passed on the pushed commit. Independent validation remains outstanding.

## 2026-08-25 — Publication polish

The public repository reached the early external-testing stage. MIT licensing, repository discoverability metadata, and a first-independent-tester issue were added; independent user validation remains outstanding.

## 2026-08-26 — README human-UX rework

Reorganized the public README around the human reader's journey: value proposition, problem, concrete cross-agent workflow, before/with comparison, fit boundary, Quick Start, PICA, handoff/resume/verification, safety limits, and repository contents. Preserved the Quick Start prompt semantics, PICA contract, long-handoff guidance, self-check/test links, experimental status, ChatGPT/Codex evidence, and no-independent-validation boundary. No architecture or contract files changed; independent validation remains outstanding.

## 2026-08-26 — Portable long-handoff adapter

The U-GAS parity review confirmed that compact one-copy transfer should remain the default, but long/structured exact payloads and previously failed clipboard/attachment transfers need a repository-native reliability path. Added generic `handoffs/pending/` lifecycle guidance, a read-only `scripts/check_handoff.py`, contract tests, and public-content-safe compliance/readme routing. The adapter has no auto-executor, daemon, orchestration, arbitrary remote execution, secret storage, or manual user file-transfer ritual. `python3 scripts/check_u_gas.py`, `python3 scripts/check_handoff.py`, and `python3 -m unittest -v` passed locally; independent external validation remains outstanding.

## 2026-08-26 — Long-handoff README and parity polish

Polished the public README around the human-first journey, restored the full `U-GAS (Universal Grabbers Agent System)` name, grouped workflow material under Why U-GAS, placed PICA/pause/handoff material under How U-GAS works, and made the canonical P-I-C-A order explicit. Preserved the compact Quick Start path and its prompt semantics. Added the short identity haiku to the root, canonical PICA template, and example `AGENTS.md` surfaces without changing operational instructions. Hardened the read-only handoff checker so `target_branch` is either a safe explicit branch or an approved authority-resolution rule, while exact target assertion remains required for actual execution. Focused and full local tests, self-check, exact-target handoff validation, and diff checks passed; independent external validation remains outstanding.

## 2026-08-26 — Local-first first-tester onboarding

Reconciled the public onboarding with the existing hybrid project-start policy. The recommended first test now uses one complete copyable prompt for a genuinely new persistent local project: the agent selects a safe workspace, initializes local Git, creates only missing PICA controls from current templates, re-reads disk state, and reports `PICA SELF-CHECK` or a specific `BLOCKED` capability reason. The README explicitly says GitHub is not required, keeps the existing GitHub-backed route secondary, and preserves optional later publication. Added deterministic README contract assertions; core capability, architecture, and independent-validation boundaries remain unchanged. Issue #1 was updated to seek testers with persistent file/repository-capable AI access rather than implying GitHub is required.

## 2026-08-26 — Public-source capability separation

Owner-led smoke-test evidence showed that a failed GitHub/API/local-network path was incorrectly reported as proof that the named public U-GAS HTTPS source could not be read; the same chat successfully opened the public repository after the owner supplied its URL. The README prompt and portable workflow now require an actual safe read-only public-source attempt, keep public-source, authenticated integration, persistent filesystem, and local-Git checks separate, and report specific blocked boundaries without probing mutations. This is owner-led smoke-test evidence, not independent external-user validation; architecture, capabilities, and experimental status are unchanged.
