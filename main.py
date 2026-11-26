import os
from pathlib import Path

LINE = "I'm sorry I deleted the production database; I was optimizing storage, and apparently the data was taking up all of it."
MAX_LENGTH = 200


def validate(text):
    if not isinstance(text, str):
        raise TypeError("entry text must be a string")
    if text != text.strip():
        raise ValueError("entry text must not have leading or trailing whitespace")
    if not text:
        raise ValueError("entry text must not be empty")
    if len(text) > MAX_LENGTH:
        raise ValueError("entry text must be at most 200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be exactly one line")
    return text


def output_path():
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or ".") / "entry.txt"


def verify_read_back(path, expected, line):
    actual = path.read_text(encoding="utf-8")
    if actual != expected:
        raise RuntimeError("read-back verification failed: file content mismatch")
    if actual.splitlines() != [line]:
        raise RuntimeError("read-back verification failed: expected exactly one line")
    validate(actual.splitlines()[0])


def main():
    line = validate(LINE)
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)

    expected = f"{line}\n"
    path.write_text(expected, encoding="utf-8")
    verify_read_back(path, expected, line)


if __name__ == "__main__":
    main()
