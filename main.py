#!/usr/bin/env python3
"""Roast Your Own Agent — entry program.

Writes one line roasting the AI agent my own team built to /output/entry.txt.
No network, no secrets, no dependencies: the roast is baked into the program.
"""

import os

ROAST = (
    "My agent burned six hours hunting a free VPS to save me $0, "
    "then charged me $47 in tokens for the victory lap."
)


def main() -> None:
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, f"roast is {len(text)} chars, must be 1-200"
    assert text.strip(), "roast must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
