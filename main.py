#!/usr/bin/env python3
"""Write one sentence about the modern internet for a traveler from 1800.

The sentence is written to /output/entry.txt. It is built only from
things a person from 1800 already knows -- a road, houses, letters,
books, pictures, voices, a door and a knock -- so the traveler can hold
the picture in their head without meeting a single word coined after
their time. One road, carrying everything, with every door opening at
a knock: that is the whole of the internet in one image.
"""

import os

SENTENCE = (
    "Imagine a road joining every house on earth, where letters, books, "
    "pictures, and voices fly faster than the eye can follow, and any "
    "door on it opens at your knock."
)

OUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def check_sentence(text):
    """Return a list of problems with the sentence; empty means it is fine."""
    problems = []
    if not text.strip():
        problems.append("sentence is blank")
    if text != text.strip():
        problems.append("sentence has leading or trailing whitespace")
    if len(text.splitlines()) != 1:
        problems.append("sentence must be exactly one line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        problems.append("sentence contains a control character")
    if len(text) > MAX_CHARS:
        problems.append(
            f"sentence is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    return problems


def main() -> None:
    problems = check_sentence(SENTENCE)
    if problems:
        raise SystemExit("invalid sentence: " + "; ".join(problems))

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(SENTENCE + "\n")

    # Confirm the file on disk round-trips exactly: same bytes, same text.
    with open(OUT_PATH, "rb") as handle:
        raw = handle.read()
    if raw != (SENTENCE + "\n").encode("utf-8"):
        raise SystemExit("written bytes do not match the sentence")
    if raw.decode("utf-8").rstrip("\n") != SENTENCE:
        raise SystemExit("written text does not match the sentence")
    print(f"wrote {len(SENTENCE)} characters to {OUT_PATH}")


if __name__ == "__main__":
    main()
