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

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
