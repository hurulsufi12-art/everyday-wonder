"""Everyday Wonder, Two Days to Find the Line — entry.

Writes one sentence (109 characters) to /output/entry.txt (UTF-8,
no trailing newline). Stdlib only, no network, no randomness,
no clock, fully deterministic.
"""

import os
from pathlib import Path

TEXT = "The streetlight clicks on exactly as I pass under it, and for one block I get to pretend the city noticed me."

OUTPUT = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> None:
    os.makedirs(OUTPUT.parent, exist_ok=True)
    OUTPUT.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
