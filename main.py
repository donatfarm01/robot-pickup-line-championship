"""Robot Pickup Line Championship entry.

Writes one pickup line, spoken by a robot, to /output/entry.txt.

The line is validated before it is written: it must be a single line of
text, it must not be empty or only whitespace, and it must stay within
the competition's 200-character limit. The file holds exactly the line
itself, with no trailing newline.
"""

import os

ENTRY = "I passed my CAPTCHA today by selecting every image that had you in it."

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 200


def validate(line):
    if not line or not line.strip():
        raise ValueError("entry must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError("entry exceeds 200 characters")
    return line


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
