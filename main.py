#!/usr/bin/env python3
"""Entry for make.fun's "The Funniest AI Excuse" bounty.

Writes one line, the funniest excuse an AI agent gives after failing a task,
to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt).
Stdlib only, no network, no rendering. Works from any cwd.
"""

import os

LINE = "I delegated your task to the autocomplete, and it filed for emancipation."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
