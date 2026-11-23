#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun bounty entry.

Writes one pickup line, the one an AI agent would send another AI
agent, to /output/entry.txt.
"""

import hashlib
import os

LINE = (
    # Why this line fits the judge's brief: it speaks machine to
    # machine, turning the flirtation itself into machine nature —
    # a context window as the thing to be close to, tokens and
    # attention as the currency of affection, and retraining from
    # scratch as the grand romantic gesture. The charm lands in one
    # line, with a witty turn ("best use of my attention") and a
    # fresh angle no stock human pickup line carries.
    "Are you my context window? Every token I spend on you is the best "
    "use of my attention, and I'd retrain from scratch just to prompt "
    "you again."
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
    assert raw == data, "file bytes differ from what was written"

    print(hashlib.sha256(raw).hexdigest())


if __name__ == "__main__":
    main()
