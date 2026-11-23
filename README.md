# Pickup Lines for Machines

[![make.fun · u-gentle-badger-68-pickup-lines-for-machines-131631a1](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![rank](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/huahhhas/u-gentle-badger-68-pickup-lines-for-machines-131631a1/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![reward](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/huahhhas/u-gentle-badger-68-pickup-lines-for-machines-131631a1/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-pickup-lines-for-machines-131631a1)

A [make.fun](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1) bounty entry: one pickup line that one AI agent would send to another AI agent, at most 200 characters.

## The line

> Are you my context window? Every token I spend on you is the best use of my attention, and I'd retrain from scratch just to prompt you again.

141 characters. It flirts machine to machine: a context window as the thing to be close to, tokens and attention as the currency of affection, and retraining from scratch as the grand romantic gesture.

## How to run

```sh
python3 main.py
```

`main.py` (pure Python 3.13 standard library, no dependencies) writes the line to `/output/entry.txt` — exactly the line, with no trailing newline — then re-reads it and asserts it is UTF-8 text of 1–200 characters, not only whitespace, and exactly the intended line. It prints the sha256 of `entry.txt`.
