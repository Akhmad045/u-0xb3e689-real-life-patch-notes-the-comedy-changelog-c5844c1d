#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch-note line to /output/entry.txt.
"""

LINE = (
    "v2.5.0: fixed a bug where crossing a doorway wiped the user's "
    "working memory of why they entered the room."
)


def main():
    import os

    if not 1 <= len(LINE) <= 160:
        raise SystemExit(f"line is {len(LINE)} characters, must be 1-160")
    if not LINE.strip():
        raise SystemExit("line must not be only whitespace")
    if "\n" in LINE:
        raise SystemExit("line must be a single line")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    with open("/output/entry.txt", "rb") as f:
        written = f.read().decode("utf-8")
    if written != LINE + "\n":
        raise SystemExit("round-trip check failed: file does not match LINE")
    print(f"wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
