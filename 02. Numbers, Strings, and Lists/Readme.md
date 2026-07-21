# Day 02 — Numbers, Strings, and Lists

## What I learned today

Moved from "how the interpreter runs" into actually writing Python. Today covered the core building blocks every program uses:

- Comments (`#`)
- Numbers — `int` vs `float`, arithmetic operators, floor division (`//`), modulo (`%`), exponents (`**`), and the special `_` variable in interactive mode
- Strings — quoting rules, escaping, raw strings, multi-line strings, concatenation, indexing, slicing, and why strings are immutable
- Lists — indexing/slicing, mutability, `.append()`, the aliasing gotcha (two variables pointing at the same list), shallow copies, slice assignment, and nested lists
- First real program logic — multiple assignment, `while` loops, comparison operators, indentation rules, and `print()` behavior (including the `end` keyword)

## Why this matters

This is the vocabulary everything else gets built from. The aliasing gotcha with lists in particular is a classic bug source — two variables can silently point at the same list, so "copying" one and editing it can change both unless you actually understand what's happening under the hood.

## Files in this folder

| File | Purpose |
|---|---|
| [`notes.md`](./notes.md) | Detailed notes on numbers, strings, lists, and basic program flow |
| [`examples.py`](./examples.py) | Runnable examples for every concept covered today |
| [`exercises.py`](./exercises.py) | Practice tasks to reinforce today's concepts |

## How to use this folder

1. Read `notes.md` first.
2. Run `examples.py` and try tweaking values to see how output changes.
3. Attempt `exercises.py` before checking notes again.

## Status

- [ ] Notes read
- [ ] Examples run and understood
- [ ] Exercises completed
