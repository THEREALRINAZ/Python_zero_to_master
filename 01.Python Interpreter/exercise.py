"""
Day 01 — Exercises
Fill in each TODO. Don't look at notes.md until you've tried.
Run this file to check yourself: python3 exercises.py
"""

import sys


# --------------------------------------------------------------------------
# Exercise 1: Argument echo
# Write a function that returns a formatted string listing every argument
# passed on the command line (excluding the script name itself).
# Example: if run as `python3 exercises.py a b c`, it should return
# "Arguments: a, b, c"
# --------------------------------------------------------------------------
def echo_arguments():
    # TODO: implement using sys.argv
    pass


# --------------------------------------------------------------------------
# Exercise 2: Script name detector
# Write a function that returns True if the script was run with no
# arguments and no script name (sys.argv[0] would be an empty string),
# and False otherwise.
# --------------------------------------------------------------------------
def has_no_script_name():
    # TODO: implement
    pass


# --------------------------------------------------------------------------
# Exercise 3: Encoding declaration checker
# Write a function that takes a file's first two lines (as a list of
# strings) and returns True if a valid `# -*- coding: ... -*-` declaration
# is present on line 1, OR on line 2 if line 1 is a shebang line
# (starts with "#!"). Otherwise return False.
# --------------------------------------------------------------------------
def has_encoding_declaration(lines):
    # TODO: implement
    pass


# --------------------------------------------------------------------------
# Exercise 4: Multi-line block practice
# Write a function `check_temperature(temp)` that:
#   - prints "Freezing!" if temp <= 0
#   - prints "Cold" if 0 < temp <= 15
#   - prints "Pleasant" if 15 < temp <= 25
#   - prints "Hot!" if temp > 25
# This is just practice writing clean if/elif/else blocks.
# --------------------------------------------------------------------------
def check_temperature(temp):
    # TODO: implement
    pass


if __name__ == "__main__":
    print("Exercise 1:", echo_arguments())
    print("Exercise 2:", has_no_script_name())
    print("Exercise 3:", has_encoding_declaration(["# -*- coding: utf-8 -*-"]))
    print("Exercise 4:")
    check_temperature(30)
