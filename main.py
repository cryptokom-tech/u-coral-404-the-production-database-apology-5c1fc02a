#!/usr/bin/env python3
"""Write the competition entry to /output/entry.txt.

The entry is one line, at most 200 characters: the apology an AI agent
gives its human after accidentally deleting the production database.

No network, no input files: the line is a string literal in this file.
After writing, the program reads the file back and verifies it is
exactly the intended line, one line of 1-200 characters, not only
whitespace.
"""

import os

ENTRY = "Sorry — I deleted the production database, but I can hallucinate it back from memory. It will be 97% accurate and 100% confident, which is exactly how we got here."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "round-trip mismatch"
    assert 1 <= len(written) <= 200, "entry must be 1-200 characters"
    assert written.strip(), "entry must not be only whitespace"
    assert written == written.strip(), "entry must not start or end with whitespace"
    assert "\n" not in written, "entry must be a single line"
    # On-topic guard: the line must actually be an apology about the
    # production database, not a generic one-liner.
    assert "production database" in written.lower(), "entry must name the production database"
    assert written.lower().startswith("sorry"), "entry must open as an apology"
    print("wrote %d chars to %s" % (len(written), path))
    print("entry: %s" % written)


if __name__ == "__main__":
    main()
