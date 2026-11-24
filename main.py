#!/usr/bin/env python3
"""Write one sentence about the modern internet for a traveler from 1800.

The sentence is written to /output/entry.txt. It uses only words and
pictures a person from 1800 would already know -- a road, houses, letters,
books, pictures, voices, a door and a knock -- so the traveler can hold
the idea in their head without any word coined after their time.
"""

import os

SENTENCE = (
    "Imagine a road joining every house on earth, where letters, books, "
    "pictures, and voices fly faster than the eye can follow, and any "
    "door on it opens at your knock."
)

OUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    text = SENTENCE

    # The gate wants one non-blank line of 1 to 200 characters.
    if not text or text != text.strip():
        raise SystemExit("sentence must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("sentence must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise SystemExit("sentence must not contain control characters")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"sentence is {len(text)} characters, over the {MAX_CHARS} limit"
        )

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")

    # Read it back and confirm what landed is exactly what we meant.
    with open(OUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written.rstrip("\n") != text:
        raise SystemExit("written file does not match the sentence")
    print(f"wrote {len(text)} characters to {OUT_PATH}")


if __name__ == "__main__":
    main()
