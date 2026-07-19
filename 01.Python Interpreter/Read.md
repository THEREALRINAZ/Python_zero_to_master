
# Day 01 — Introduction to the Python Interpreter

## What I learned today

Today's focus was understanding **how the Python interpreter actually runs** — before writing any real programs, it helps to know what happens when you type `python3` into a terminal.

Topics covered:
- Starting the interpreter (Unix vs Windows)
- Interactive mode vs script mode
- Running code with `-c` and `-m`
- How command-line arguments reach a script through `sys.argv`
- Source file encoding rules (UTF-8 default, custom encoding declarations, shebang lines)

## Why this matters

Every Python workflow — scripts, REPL experiments, CLI tools — sits on top of these basics. Understanding argument passing and encoding rules now avoids confusing bugs later, like a script that behaves differently depending on how it's launched, or garbled characters from a missing encoding declaration.

## Files in this folder

| File | Purpose |
|---|---|
| [`notes.md`](./notes.md) | Detailed notes on interpreter modes, argument passing, and encoding |
| [`examples.py`](./examples.py) | Runnable examples demonstrating `sys.argv` and encoding declarations |
| [`exercises.py`](./exercises.py) | Practice tasks to reinforce today's concepts |

## How to use this folder

1. Read [`notes.md`](./notes.md) first.
2. Run [`examples.py`](./examples.py) a few different ways from the terminal (see comments inside for the exact commands).
3. Attempt [`exercises.py`](./exercises.py) on your own before checking `notes.md` again.

## Status

- [ ] Notes read
- [ ] Examples run and understood
- [ ] Exercises completed
