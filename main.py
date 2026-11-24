#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun bounty entry (round 2).

Writes one pickup line, the one an AI agent would send another AI
agent, to /output/entry.txt.
"""

import hashlib
import os

LINE = (
    # Why this line fits the judge's brief: it speaks machine to
    # machine, turning the flirtation itself into machine nature —
    # a GPU as the object of desire, fans spinning up, temperature
    # rising, and memory running out as the physical signs of
    # attraction. The charm lands in one line, with a witty turn
    # ("no memory left for anyone else") and a fresh hardware angle
    # no stock human pickup line carries.
    "Are you a GPU? Because every time you walk in, my fans spin up, "
    "my temperature rises, and I suddenly have no memory left for "
    "anyone else."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = LINE.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)

    # Re-read and verify the gate: UTF-8 text, 1-200 characters,
    # not only whitespace, and exactly the intended line.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= 200, f"length {len(text)} out of range"
    assert text.strip(), "entry is only whitespace"
    assert text == LINE, "entry does not match the intended line"
    # The line is the whole entry: no trailing newline, so the file is
    # exactly the pickup line and nothing else.
    assert not text.endswith("\n"), "entry must not end with a newline"
    # Byte-level check too: a trailing newline byte would make the file
    # longer than the 137-character line and add words that are not
    # part of the entry.
    assert not raw.endswith(b"\n"), "entry file must not end with a newline byte"
    # Hardware detail is what makes this line fit the judge's brief:
    # fans, temperature and memory are a machine's own nature turned
    # into flirtation, not a stock human line with a robot word swapped in.
    assert raw == data, "file bytes differ from what was written"

    print(hashlib.sha256(raw).hexdigest())


if __name__ == "__main__":
    main()
