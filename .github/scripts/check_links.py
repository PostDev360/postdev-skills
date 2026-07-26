#!/usr/bin/env python3
"""Check that every relative Markdown link in the repo resolves to a real file.

External links (http, mailto) and pure anchors are skipped — this only catches
the class of breakage that renames and moves cause.

Usage:  python3 .github/scripts/check_links.py
Exit code 0 if every link resolves, 1 otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

REPO_ROOT = Path(__file__).resolve().parents[2]
SKIP_DIRS = {".git", "node_modules", "__pycache__"}

# [text](target) — target captured up to the closing paren, no nested parens.
LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "#", "//"))


def check_file(path: Path) -> list[str]:
    errors: list[str] = []
    rel = path.relative_to(REPO_ROOT)
    text = path.read_text(encoding="utf-8", errors="replace")

    for target in LINK_PATTERN.findall(text):
        if is_external(target):
            continue
        # strip any anchor, then percent-decode
        file_part = unquote(target.split("#", 1)[0])
        if not file_part:
            continue
        resolved = (path.parent / file_part).resolve()
        if not resolved.exists():
            errors.append(f"{rel}: broken relative link -> {target}")

    return errors


def main() -> int:
    md_files = sorted(
        p
        for p in REPO_ROOT.rglob("*.md")
        if not SKIP_DIRS.intersection(p.relative_to(REPO_ROOT).parts)
    )

    errors: list[str] = []
    for path in md_files:
        errors.extend(check_file(path))

    if errors:
        print(f"{len(errors)} broken link(s) found:\n")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"All relative links in {len(md_files)} Markdown file(s) resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
