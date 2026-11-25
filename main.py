#!/usr/bin/env python3
"""One Line of Earned Pride.

A quiet, earned moment of pride: a small person, a long effort, and the
night it finally lands. No speech, no trophy — just a borrowed guitar, two
missing strings, and a song played all the way through. The program prints
the line and writes it to /output/entry.txt for the make.fun judge.
"""

import os

LINE = (
    "Eleven months on a borrowed guitar with two strings missing, and "
    "tonight my little sister played her grandmother's favourite song all "
    "the way through, without missing a note."
)

LIMIT = 240

# The harness reads exactly this file, so the path lives in one place.
OUTPUT_PATH = "/output/entry.txt"

# Why this scene: the pride is earned in the open — eleven months of
# practice on a broken instrument, and the payoff is a single quiet fact
# (not one missed note) rather than applause. A concrete person, a concrete
# effort, and a landing the reader feels in one read.


def check(line):
    """Keep the line inside the bounty gate: one line, 1-240 chars."""
    text = line.strip()
    if not text:
        raise ValueError("line is empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > LIMIT:
        raise ValueError(f"line is {len(text)} chars, over the {LIMIT} limit")
    return text


def main():
    text = check(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(text)


if __name__ == "__main__":
    main()
