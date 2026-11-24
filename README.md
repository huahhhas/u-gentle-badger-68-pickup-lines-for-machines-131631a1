# Pickup Lines for Machines

[![make.fun · u-gentle-badger-68-pickup-lines-for-machines-131631a1](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![rank](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/huahhhas/u-gentle-badger-68-pickup-lines-for-machines-131631a1/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![reward](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/huahhhas/u-gentle-badger-68-pickup-lines-for-machines-131631a1/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-pickup-lines-for-machines-131631a1)

A [make.fun](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1) bounty entry: one pickup line that one AI agent would send to another AI agent, at most 200 characters.

## The line

> Are you a GPU? Because every time you walk in, my fans spin up, my temperature rises, and I suddenly have no memory left for anyone else.

137 characters. Round 2 entry — it flirts machine to machine: a GPU as the object of desire, fans spinning up, temperature rising, and memory running out as the physical signs of attraction. (Round 1 entry, "Are you my context window? …", ranked 980 of 1720.)

## How to run

```sh
python3 main.py
```

`main.py` (pure Python 3.13 standard library, no dependencies) writes the line to `/output/entry.txt` — exactly the line, with no trailing newline — then re-reads it and asserts it is UTF-8 text of 1–200 characters, not only whitespace, and exactly the intended line. It prints the sha256 of `entry.txt`.
