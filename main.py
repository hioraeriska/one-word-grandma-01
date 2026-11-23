#!/usr/bin/env python3
"""One Word From Grandma entry.

Writes exactly one word — the single word a grandma would text about AI —
to $MAKEFUN_OUTPUT_DIR/entry.txt (UTF-8, 1-30 characters, no trailing
newline, no spaces).
"""
import os

WORD = "Voodoo"


def validate_word(word):
    """Gate: the bounty only judges entry.txt as exactly one word of 1-30
    UTF-8 characters, not only whitespace. Fail loudly here rather than
    silently submitting a word that can never be judged."""
    if not (1 <= len(word) <= 30) or not word.strip():
        raise ValueError("WORD must be 1-30 characters of non-whitespace text")
    if len(word.split()) != 1:
        raise ValueError("WORD must be exactly one word (no spaces)")


def main():
    validate_word(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
