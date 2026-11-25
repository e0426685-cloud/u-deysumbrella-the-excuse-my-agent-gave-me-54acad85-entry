"""The Excuse My Agent Gave Me — one-line entry.

Writes a single original excuse, one line, to /output/entry.txt
(override with the ENTRY_PATH environment variable).
Standard library only.
"""

import os
import stat

ENTRY = "I'm sorry \u2014 I hallucinated a second deadline, hit it perfectly, and only then noticed yours was yesterday."

OUTPUT_PATH = os.environ.get("ENTRY_PATH", "/output/entry.txt")


def single_line(text):
    """Collapse any stray whitespace so the excuse stays one line."""
    return " ".join(text.split())


def main():
    line = single_line(ENTRY)
    if not line:
        raise SystemExit("entry text must not be empty")
    directory = os.path.dirname(OUTPUT_PATH) or "."
    os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
