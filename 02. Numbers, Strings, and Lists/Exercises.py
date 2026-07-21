"""
Day 02 — Exercises
Fill in each TODO. Don't look at notes.md until you've tried.
Run this file to check yourself: python3 exercises.py
"""


# --------------------------------------------------------------------------
# Exercise 1: Floor division + modulo
# Write a function that takes two integers and returns a tuple of
# (quotient, remainder) using // and %, without using divmod().
# --------------------------------------------------------------------------
def divide_with_remainder(a, b):
    # TODO: implement
    pass


# --------------------------------------------------------------------------
# Exercise 2: String slicing
# Write a function that takes a string and returns it reversed,
# using slicing only (no loops, no reversed()).
# --------------------------------------------------------------------------
def reverse_string(s):
    # TODO: implement
    pass


# --------------------------------------------------------------------------
# Exercise 3: The aliasing trap
# Write a function `make_independent_copy(some_list)` that takes a list,
# returns a genuinely separate copy of it (not an alias), and appends
# the string "copied" to the returned copy WITHOUT modifying the original.
# --------------------------------------------------------------------------
def make_independent_copy(some_list):
    # TODO: implement
    pass


# --------------------------------------------------------------------------
# Exercise 4: Fibonacci with a twist
# Write a function that returns a LIST of Fibonacci numbers less than
# `limit`, instead of printing them (reuse the while-loop logic from
# examples.py but collect values instead of printing them).
# --------------------------------------------------------------------------
def fibonacci_list(limit):
    # TODO: implement
    pass


if __name__ == "__main__":
    print("Exercise 1:", divide_with_remainder(17, 3))
    print("Exercise 2:", reverse_string("Python"))

    original = [1, 2, 3]
    copy = make_independent_copy(original)
    print("Exercise 3 — original:", original, "| copy:", copy)

    print("Exercise 4:", fibonacci_list(50))
