#!/usr/bin/env python3
"""Pure helpers for the visible U-GAS PICA contract."""
from __future__ import annotations

from pathlib import Path

PICA_FILES = ("AGENTS.md", "CURRENT_STATE.md", "PROGRESS.md", "IDEAS.md")
TEMPLATE_FILES = PICA_FILES
CANONICAL_UPSTREAM = "https://github.com/jaabster-dev/u-gas"


def missing_pica(root_files):
    """Return missing canonical PICA names without changing anything."""
    present = set(root_files or [])
    return [name for name in PICA_FILES if name not in present]


def template_root(repo_root=None):
    root = Path(repo_root) if repo_root else Path(__file__).resolve().parents[1]
    return root / "templates" / "pica"


def load_templates(repo_root=None):
    """Load complete canonical template text, keyed by PICA filename."""
    base = template_root(repo_root)
    return {name: (base / name).read_text(encoding="utf-8") for name in TEMPLATE_FILES}


def preserve_substantive(existing_text, template_text):
    """Return existing content unchanged; templates never overwrite it."""
    return existing_text if existing_text is not None else template_text
