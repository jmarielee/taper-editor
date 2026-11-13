#!/usr/bin/env python3
"""Fail if any file in react/ contains a raw hex color or a px value.

Allowed px values:
- 22px, the VerdictBanner icon width, in react/VerdictBanner.css only.
- 12px, the SeverityTag icon width, in react/SeverityTag.css only.

Usage: python3 check-tokens.py   (exit 0 = clean, 1 = violations)
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = HERE / "react"

HEX = re.compile(r"#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})\b")
PX = re.compile(r"(?<![\w.-])-?(\d*\.?\d+)px\b", re.IGNORECASE)
ALLOWED_PX = set()
# Exceptions allowed only in one file, keyed by path relative to this script.
ALLOWED_PX_IN_FILE = {
    "react/VerdictBanner.css": {"22"},
    "react/SeverityTag.css": {"12"},
}


def main():
    files = sorted(p for p in TARGET.rglob("*") if p.is_file() and p.name != ".DS_Store")
    if not files:
        sys.exit(f"No files found in {TARGET}")

    problems = []
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        rel = path.relative_to(HERE)
        allowed = ALLOWED_PX | ALLOWED_PX_IN_FILE.get(rel.as_posix(), set())
        for lineno, line in enumerate(text.splitlines(), 1):
            for m in HEX.finditer(line):
                problems.append(f"{rel}:{lineno}: raw hex color {m.group(0)}")
            for m in PX.finditer(line):
                if m.group(1) not in allowed:
                    problems.append(f"{rel}:{lineno}: px value {m.group(0)}")

    if problems:
        print("\n".join(problems))
        print(f"\nFAIL: {len(problems)} problem(s). Use tokens from build/tokens.css instead.")
        sys.exit(1)
    print(f"OK: {len(files)} file(s) in {TARGET.relative_to(HERE)}/ use tokens only.")


if __name__ == "__main__":
    main()
