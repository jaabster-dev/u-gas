#!/usr/bin/env python3
"""Read-only local Git branch-health preflight for a U-GAS project."""
from __future__ import annotations
import argparse, subprocess
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Result:
    status: str
    authority_branch: str
    release_branch: str | None
    authority_ahead: int | None
    release_ahead: int | None
    note: str

def git(repo: Path, *args: str) -> str:
    run = subprocess.run(["git", "-C", str(repo), *args], text=True, capture_output=True)
    if run.returncode:
        raise RuntimeError((run.stderr or run.stdout).strip() or "git command failed")
    return run.stdout.strip()

def evaluate(repo: Path, authority_branch: str, release_branch: str | None = None) -> Result:
    try:
        git(repo, "rev-parse", "--git-dir")
        git(repo, "rev-parse", "--verify", authority_branch)
        if not release_branch or release_branch == authority_branch:
            return Result("GREEN", authority_branch, release_branch, 0 if release_branch else None, 0 if release_branch else None, "authority branch resolved")
        git(repo, "rev-parse", "--verify", release_branch)
        counts = git(repo, "rev-list", "--left-right", "--count", f"{release_branch}...{authority_branch}").split()
        if len(counts) != 2:
            raise RuntimeError("branch comparison returned incomplete counts")
        release_ahead, authority_ahead = map(int, counts)
        if release_ahead:
            return Result("RED", authority_branch, release_branch, authority_ahead, release_ahead, "release branch contains commits outside the authority branch")
        return Result("GREEN", authority_branch, release_branch, authority_ahead, release_ahead, "release branch is contained in authority branch")
    except (RuntimeError, ValueError) as exc:
        return Result("ERROR", authority_branch, release_branch, None, None, str(exc))

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--authority-branch", required=True)
    parser.add_argument("--release-branch")
    args = parser.parse_args(argv)
    result = evaluate(args.repo, args.authority_branch, args.release_branch)
    print(f"REPOSITORY HEALTH: {result.status}")
    print(f"authority: {result.authority_branch}")
    print(f"release: {result.release_branch or '-'}")
    if result.authority_ahead is not None:
        print(f"authority-ahead: {result.authority_ahead}")
        print(f"release-ahead: {result.release_ahead}")
    print(f"note: {result.note}")
    return 0 if result.status == "GREEN" else 1

if __name__ == "__main__":
    raise SystemExit(main())
