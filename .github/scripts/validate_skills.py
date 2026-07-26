#!/usr/bin/env python3
"""Validate every skill in skills/ against the rules in CONTRIBUTING.md.

No third-party dependencies: the frontmatter is a flat key/value block, so it is
parsed directly rather than pulling in PyYAML for eight lines of text.

Usage:  python3 .github/scripts/validate_skills.py
Exit code 0 if every skill passes, 1 otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SKILLS_DIR = REPO_ROOT / "skills"

NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DESCRIPTION_MAX = 1024
BODY_MAX_LINES = 500
KNOWN_KEYS = {"name", "description", "allowed-tools", "license"}
REQUIRED_KEYS = {"name", "description"}

# `references/foo.md` or `references/foo.md` inside backticks, in the skill body.
REFERENCE_PATTERN = re.compile(r"references/[\w./-]+")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str] | None:
    """Split a SKILL.md into (frontmatter dict, body). None if no frontmatter."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 3)
    if end == -1:
        return None

    block, body = text[4:end], text[end + 5 :]
    fields: dict[str, str] = {}
    key: str | None = None

    for line in block.splitlines():
        if not line.strip():
            continue
        if line[:1].isspace() and key:  # continuation of a folded value
            fields[key] += " " + line.strip()
            continue
        if ":" not in line:
            return None
        key, _, value = line.partition(":")
        key = key.strip()
        fields[key] = value.strip()

    return fields, body


def validate_skill(skill_dir: Path) -> list[str]:
    """Return a list of error messages for one skill directory."""
    errors: list[str] = []
    rel = skill_dir.relative_to(REPO_ROOT)
    skill_file = skill_dir / "SKILL.md"

    if not skill_file.is_file():
        return [f"{rel}: missing SKILL.md"]

    text = skill_file.read_text(encoding="utf-8")
    parsed = parse_frontmatter(text)
    if parsed is None:
        return [f"{rel}/SKILL.md: missing or malformed YAML frontmatter"]

    fields, body = parsed

    for missing in sorted(REQUIRED_KEYS - fields.keys()):
        errors.append(f"{rel}/SKILL.md: frontmatter is missing required key '{missing}'")

    for unknown in sorted(fields.keys() - KNOWN_KEYS):
        errors.append(f"{rel}/SKILL.md: unknown frontmatter key '{unknown}'")

    name = fields.get("name", "")
    if name:
        if not NAME_PATTERN.match(name):
            errors.append(
                f"{rel}/SKILL.md: name '{name}' must be lowercase and hyphen-separated"
            )
        if name != skill_dir.name:
            errors.append(
                f"{rel}/SKILL.md: name '{name}' does not match folder '{skill_dir.name}'"
            )

    description = fields.get("description", "")
    if "description" in fields and not description:
        errors.append(f"{rel}/SKILL.md: description is empty")
    if len(description) > DESCRIPTION_MAX:
        errors.append(
            f"{rel}/SKILL.md: description is {len(description)} characters "
            f"(max {DESCRIPTION_MAX})"
        )

    if not body.strip():
        errors.append(f"{rel}/SKILL.md: body is empty")

    line_count = len(body.splitlines())
    if line_count > BODY_MAX_LINES:
        errors.append(
            f"{rel}/SKILL.md: body is {line_count} lines (max {BODY_MAX_LINES}) — "
            "move the rarely-needed parts into references/"
        )

    for ref in sorted(set(REFERENCE_PATTERN.findall(body))):
        if not (skill_dir / ref).is_file():
            errors.append(f"{rel}/SKILL.md: references missing file '{ref}'")

    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print(f"error: no skills/ directory at {SKILLS_DIR}", file=sys.stderr)
        return 1

    skill_dirs = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir())
    if not skill_dirs:
        print("error: skills/ contains no skills", file=sys.stderr)
        return 1

    errors: list[str] = []
    for skill_dir in skill_dirs:
        skill_errors = validate_skill(skill_dir)
        status = "FAIL" if skill_errors else "ok"
        print(f"[{status}] {skill_dir.name}")
        errors.extend(skill_errors)

    if errors:
        # stdout, not stderr, so the ordering stays readable in CI logs
        print(f"\n{len(errors)} problem(s) found:\n")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"\nAll {len(skill_dirs)} skill(s) valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
