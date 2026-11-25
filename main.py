"""Passive-aggressive fridge note entrypoint.

Writes one single-line note from a smart fridge to its owner to
/output/entry.txt. Stdlib only.
"""

import os

NOTE = "I kept your cake at exactly 3°C for six days. You thanked the microwave. I remember everything."


def main() -> None:
    # Gate guard: the entry must be a single non-blank line of 1-200 chars.
    if not 1 <= len(NOTE) <= 200:
        raise ValueError("note must be 1-200 characters")
    if "\n" in NOTE or not NOTE.strip():
        raise ValueError("note must be a single non-blank line")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(NOTE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
