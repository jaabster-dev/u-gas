#!/usr/bin/env python3
"""Read-only generic checker for repository-backed pending handoffs."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPOSITORY_PATTERN = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
BRANCH_NAME_PATTERN = re.compile(r"^(?!/)(?!.*//)(?!.*\.\.)[A-Za-z0-9._/-]{1,200}(?<!/)$")
BRANCH_RULE_PATTERN = re.compile(r"^resolve from current (?:[A-Za-z0-9._/-]+ )?authority(?: \(currently [A-Za-z0-9._/-]+\))?$")
REQUIRED_METADATA = ("id", "status", "created", "target_repository", "target_branch")
REQUIRED_SECTIONS = (
    "Objective", "Execution instructions", "Constraints", "Required verification",
    "Completion / consumption rule",
)
SECRET_MARKERS = (
    "BEGIN " + "PRIVATE KEY", "gh" + "p_", "github_" + "pat_", "s" + "k-",
)


def parse_contract(path: Path):
    text = path.read_text(encoding="utf-8")
    metadata = {}
    for line in text.splitlines():
        match = re.match(r"^- ([a-z_]+):\s*(.+)$", line)
        if match:
            metadata[match.group(1)] = match.group(2).strip()
    sections = {}
    current = None
    for line in text.splitlines():
        heading = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if heading:
            current = heading.group(1)
            sections[current] = []
        elif current:
            sections[current].append(line)
    return metadata, {key: "\n".join(value).strip() for key, value in sections.items()}, text


def validate_file(path: Path, expected_target: str | None = None):
    errors = []
    try:
        metadata, sections, text = parse_contract(path)
    except (OSError, UnicodeError) as exc:
        return [f"{path}: cannot read: {exc}"]
    for key in REQUIRED_METADATA:
        if key not in metadata:
            errors.append(f"{path}: missing metadata: {key}")
    if metadata.get("status") != "PENDING":
        errors.append(f"{path}: status must be exactly PENDING")
    target = metadata.get("target_repository", "")
    if not REPOSITORY_PATTERN.fullmatch(target):
        errors.append(f"{path}: target_repository must be a syntactically valid owner/repo")
    elif expected_target is not None and target != expected_target:
        errors.append(f"{path}: target_repository must be exactly {expected_target}")
    target_branch = metadata.get("target_branch", "")
    if not BRANCH_NAME_PATTERN.fullmatch(target_branch) and not BRANCH_RULE_PATTERN.fullmatch(target_branch):
        errors.append(f"{path}: target_branch must be an explicit branch name or an approved authority-resolution rule")
    handoff_id = metadata.get("id", "")
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{2,80}", handoff_id):
        errors.append(f"{path}: id is not a safe stable identifier")
    elif path.stem != handoff_id:
        errors.append(f"{path}: filename stem must equal id")
    for section in REQUIRED_SECTIONS:
        if not sections.get(section):
            errors.append(f"{path}: section is missing or empty: {section}")
    for marker in SECRET_MARKERS:
        if marker in text:
            errors.append(f"{path}: obvious secret marker is forbidden: {marker}")
    return errors


def validate_directory(directory: Path, expected_target: str | None = None):
    if not directory.is_dir():
        return [f"{directory}: pending handoff directory is missing"]
    files = sorted(directory.glob("*.md"))
    errors = []
    seen = {}
    for path in files:
        errors.extend(validate_file(path, expected_target))
        try:
            metadata, _, _ = parse_contract(path)
        except (OSError, UnicodeError):
            continue
        handoff_id = metadata.get("id")
        if handoff_id:
            seen.setdefault(handoff_id, []).append(path)
    for handoff_id, paths in seen.items():
        if len(paths) > 1:
            errors.append(f"duplicate active handoff id: {handoff_id}")
    return errors


def validate_exact_handoff(directory: Path, handoff_id: str, expected_target: str):
    """Validate one pending payload for launcher issuance."""
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{2,80}", handoff_id):
        return [f"handoff id is not a safe stable identifier: {handoff_id}"]
    if not directory.is_dir():
        return [f"{directory}: pending handoff directory is missing"]
    path = directory / f"{handoff_id}.md"
    if not path.is_file():
        return [f"{path}: exact pending handoff does not exist"]
    errors = validate_file(path, expected_target)
    for other in sorted(directory.glob("*.md")):
        if other == path:
            continue
        try:
            metadata, _, _ = parse_contract(other)
        except (OSError, UnicodeError):
            continue
        if metadata.get("id") == handoff_id:
            errors.append(f"duplicate active handoff id: {handoff_id}")
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", nargs="?", type=Path, default=Path("handoffs/pending"))
    parser.add_argument("--target", default=None, help="optional exact target repository assertion")
    parser.add_argument("--handoff-id", default=None, help="validate exactly handoffs/pending/<id>.md for launcher readiness")
    args = parser.parse_args(argv)
    if args.handoff_id is not None:
        if not args.target:
            parser.error("--target is required with --handoff-id")
        errors = validate_exact_handoff(Path("handoffs/pending"), args.handoff_id, args.target)
        if errors:
            for error in errors:
                print(f"ERROR: {error}", file=sys.stderr)
            return 1
        print(f"HANDOFF_READY: {args.handoff_id} -> {args.target}")
        return 0
    errors = validate_directory(args.directory, args.target)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"PENDING_HANDOFFS_VALID: {len(list(args.directory.glob('*.md')))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
