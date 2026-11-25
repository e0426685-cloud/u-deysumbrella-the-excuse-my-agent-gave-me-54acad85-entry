"""The Excuse My Agent Gave Me — one-line entry.

Writes a single original excuse, one line, to /output/entry.txt.
Standard library only.
"""

import os
import stat

ENTRY = "I'm sorry \u2014 I hallucinated a second deadline, hit it perfectly, and only then noticed yours was yesterday."


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
