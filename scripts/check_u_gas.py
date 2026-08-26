#!/usr/bin/env python3
"""Read-only deterministic U-GAS distribution and project self-check."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from pica_contract import CANONICAL_UPSTREAM, PICA_FILES, missing_pica, load_templates

ROOT = Path(__file__).resolve().parents[1]
AI_FILES = (
    "ai/README.md", "ai/GOVERNANCE.md", "ai/GITHUB_WORKFLOW.md",
    "ai/SESSION_CONTINUITY.md", "ai/LARGE_FILE_PATCHING.md",
    "ai/MULTI_AGENT_COLLABORATION.md", "ai/REPOSITORY_STRUCTURE.md",
    "ai/COMPLIANCE.md",
)
SKILL_FILES = (
    "skills/u-gas-resume/SKILL.md", "skills/u-gas-safe-patch/SKILL.md",
    "skills/u-gas-verify-change/SKILL.md", "skills/u-gas-external-research/SKILL.md",
    "skills/u-gas-skill-review/SKILL.md",
)
ROUTE_TARGETS = (
    "ai/GOVERNANCE.md", "ai/GITHUB_WORKFLOW.md", "ai/SESSION_CONTINUITY.md",
    "ai/LARGE_FILE_PATCHING.md", "ai/MULTI_AGENT_COLLABORATION.md",
    "ai/REPOSITORY_STRUCTURE.md", "ai/COMPLIANCE.md",
    "skills/u-gas-resume/SKILL.md", "skills/u-gas-safe-patch/SKILL.md",
    "skills/u-gas-verify-change/SKILL.md", "skills/u-gas-external-research/SKILL.md",
    "skills/u-gas-skill-review/SKILL.md", "scripts/check_u_gas.py",
)
PRIVATE_PATH = "/" + "Users/"
WORKSPACE_PATH = "~/" + "Documents/GitHub"
FORBIDDEN = re.compile(
    re.escape(PRIVATE_PATH) + r"[^\s`]+|" + re.escape(WORKSPACE_PATH) + r"|"
    + re.escape("gh" + "p_") + r"[A-Za-z0-9]|" + re.escape("github_" + "pat_")
    + r"|BEGIN [A-Z ]*PRIVATE KEY|(^|[^A-Za-z0-9])s" + r"k-[A-Za-z0-9]"
)


def read(root, relative):
    path = root / relative
    return path.read_text(encoding="utf-8") if path.is_file() else None


def check_project(root):
    errors = []
    if not root.is_dir():
        return ["project path is not a directory"]
    missing = missing_pica([p.name for p in root.iterdir()])
    if missing:
        errors.append("missing PICA: " + ", ".join(missing))
    contents = {}
    for name in PICA_FILES:
        text = read(root, name)
        if text is None:
            if name not in missing:
                errors.append(f"{name} is not readable")
            continue
        contents[name] = text
        if not text.strip():
            errors.append(f"{name} is empty")

    agents = contents.get("AGENTS.md")
    if agents is not None and CANONICAL_UPSTREAM not in agents:
        errors.append("AGENTS.md has no canonical U-GAS upstream anchor")

    current = contents.get("CURRENT_STATE.md")
    if current and current.strip():
        template = load_templates()["CURRENT_STATE.md"].strip()
        resume_patterns = (r"\bACTIVE\b", r"\bNEXT\b", r"WAITING\s*/\s*PAUSED", r"BLOCKERS\s*/\s*BOUNDARIES")
        if current.strip() != template and not all(re.search(pattern, current) for pattern in resume_patterns):
            errors.append("CURRENT_STATE.md lacks the canonical minimal placeholder or resume responsibilities")
    return errors


def check_distribution(root=ROOT):
    errors = []
    required = PICA_FILES + ("README.md", "LICENSE") + AI_FILES + SKILL_FILES
    required += ("handoffs/README.md", "handoffs/pending/.gitkeep", "scripts/check_handoff.py")
    required += tuple("templates/pica/" + name for name in PICA_FILES)
    required += tuple("examples/first-project/" + name for name in PICA_FILES)
    for relative in required:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")

    agents = read(root, "AGENTS.md") or ""
    for target in ROUTE_TARGETS:
        if target not in agents:
            errors.append(f"AGENTS route missing: {target}")
        elif not (root / target).exists():
            errors.append(f"AGENTS route target absent: {target}")

    try:
        templates = load_templates(root)
    except (OSError, UnicodeError) as exc:
        errors.append(f"templates unreadable: {exc}")
        templates = {}
    if templates:
        if CANONICAL_UPSTREAM not in templates["AGENTS.md"]:
            errors.append("template AGENTS.md missing exact canonical upstream")
        for name, text in templates.items():
            if not text.strip():
                errors.append(f"empty template: {name}")
        for name, phrase in (("CURRENT_STATE.md", "Quiet page at dawn"), ("PROGRESS.md", "Footprints wait in snow"), ("IDEAS.md", "Empty shelf, open")):
            if phrase not in templates[name]:
                errors.append(f"template haiku missing: {name}")

    for name in PICA_FILES:
        if not (root / "examples" / "first-project" / name).is_file():
            errors.append(f"example PICA missing: {name}")
    readme = read(root, "README.md") or ""
    for phrase in ("EXPERIMENTAL", "NO INDEPENDENT USER VALIDATION YET", "PICA SELF-CHECK", "Issue #1"):
        if phrase not in readme:
            errors.append(f"README marker missing: {phrase}")

    operational = []
    for relative in required:
        text = read(root, relative)
        if text:
            operational.append((relative, text))
    for relative, text in operational:
        if FORBIDDEN.search(text):
            errors.append(f"forbidden private marker in {relative}")
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=Path, help="Read-only check of another project directory")
    args = parser.parse_args(argv)
    errors = check_project(args.project) if args.project else check_distribution()
    if errors:
        print("U-GAS SELF-CHECK: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("U-GAS SELF-CHECK: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
