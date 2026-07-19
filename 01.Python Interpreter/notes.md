# Day 01 Notes — The Python Interpreter

## 1. Starting the Interpreter

On Unix-based systems, the interpreter usually lives at `/usr/local/bin/python3.14`. If that folder is on your shell's `PATH`, you can start it by just typing:

```bash
python3.14
```

The exact path can vary by installation — some setups use `/usr/local/python` instead — so it's worth checking with `which python3` if the command isn't found.

On Windows, if Python was installed from the Microsoft Store, the `python3.14` command works directly. If the `py.exe` launcher is installed instead, the `py` command is used to start it.

To exit the interpreter:
- Unix: press `Ctrl-D` (end-of-file character)
- Windows: press `Ctrl-Z` then Enter
- Or, on any platform, type `quit()` and press Enter

The interpreter also supports command history and line editing on most systems — for example, pressing the left arrow key while typing should move the cursor back rather than just printing a raw character.

## 2. Two Ways the Interpreter Can Run

The interpreter behaves like a Unix shell in one important way: it checks how it was invoked.

- **Interactive mode** — when input comes from a terminal (a tty), it reads and runs one command at a time, printing results immediately.
- **Script mode** — when given a filename, or when input is redirected from a file, it reads and executes the whole file as a script.

There are two extra ways to run code directly from the command line without a script file:

```bash
python3 -c "print('hello')"     # runs the given statement(s) directly
python3 -m http.server           # runs a module as if it were a script
```

Because shells treat spaces and quotes specially, it's safest to wrap the `-c` command in quotes.

There's also a hybrid option: adding `-i` before a script name runs the script first and then drops into interactive mode afterward — useful for inspecting variables right after a script finishes.

## 3. Command-Line Arguments (`sys.argv`)

Whatever arguments follow the script name on the command line get collected into a list called `sys.argv`, available after `import sys`.

Key rules:
- `sys.argv[0]` is normally the script's name.
- If no script and no arguments were given, `sys.argv[0]` is an empty string.
- If the script name is `-` (meaning "read from standard input"), `sys.argv[0]` becomes `'-'`.
- With `python -c command`, `sys.argv[0]` becomes `'-c'`.
- With `python -m module`, `sys.argv[0]` becomes the module's full name.
- Anything typed *after* the `-c` command or `-m` module name is left alone for that command/module to handle — Python's own option parser doesn't touch it.

## 4. What Interactive Mode Looks Like

In interactive mode, the interpreter shows a version banner, then prompts with `>>>` for a new statement and `...` for a line that continues a multi-line block (like the body of an `if` statement). Nothing needs to be memorized here beyond recognizing these prompts when working in the REPL.

## 5. Source Code Encoding

By default, Python 3 source files are assumed to be UTF-8. That's usually fine — UTF-8 covers virtually every character needed for identifiers, strings, and comments.

To use a different encoding, the **first line** of the file should declare it:

```python
# -*- coding: encoding-name -*-
```

**Exception:** if the file starts with a Unix "shebang" line (e.g. `#!/usr/bin/env python3`), the encoding declaration goes on the **second** line instead, since the shebang must stay first:

```python
#!/usr/bin/env python3
# -*- coding: cp1252 -*-
```

This mostly matters when working with legacy files or files written on systems with a non-UTF-8 default encoding.

## Summary

The interpreter isn't just "the thing that runs my code" — how it's invoked (interactively, as a script, via `-c`/`-m`) and how arguments/encoding are handled are all things that quietly affect how a program behaves depending on the environment it runs in.
