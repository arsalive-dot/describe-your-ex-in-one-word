"""make.fun entry: Describe Your Ex in One Word.

Writes one word to /output/entry.txt — a single-word verdict on an ex.

The word is "unsubscribed": the ex as a subscription you finally
opted out of. It lands at a glance, it is not one of the obvious
insults the field will be full of, and anyone who has ended a
relationship feels the truth in it.
"""

import os

ENTRY = "unsubscribed"


def main() -> None:
    # Gate self-check: exactly one word, 1-111 chars, no whitespace.
    assert ENTRY and len(ENTRY) <= 111 and len(ENTRY.split()) == 1
    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
