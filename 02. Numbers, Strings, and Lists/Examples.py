"""
Day 02 — Examples
Run this file directly: python3 examples.py
Each function is self-contained — read the print statements to see
what each concept actually produces.
"""


def numbers_demo():
    print("-- numbers --")
    print("17 / 3 =", 17 / 3)     # true division -> float
    print("17 // 3 =", 17 // 3)   # floor division -> int
    print("17 % 3 =", 17 % 3)     # remainder
    print("5 ** 2 =", 5 ** 2)     # power

    # the "_" trick only works in the interactive shell, not in scripts —
    # this just simulates the idea manually
    tax = 12.5 / 100
    price = 100.50
    subtotal = price * tax
    total = price + subtotal
    print("price * tax =", subtotal)
    print("price + subtotal =", total)


def strings_demo():
    print("\n-- strings --")
    word = "Python"
    print("word[0] =", word[0])
    print("word[-1] =", word[-1])
    print("word[0:2] =", word[0:2])
    print("word[:2] =", word[:2])
    print("word[4:] =", word[4:])

    raw = r"C:\test\node"
    interpreted = "C:\test\node"  # \t becomes a tab, \n becomes a newline
    print("raw string:      ", raw)
    print("interpreted string:", interpreted)

    joined = "un" * 3 + "ium"
    print("'un' * 3 + 'ium' =", joined)


def lists_demo():
    print("\n-- lists --")
    original = ["Red", "Green", "Blue"]
    alias = original          # NOT a copy — same list, two names
    alias.append("Alpha")
    print("original after modifying alias:", original)

    real_copy = original[:]   # actual independent copy
    real_copy.append("Beta")
    print("original after modifying real_copy:", original)
    print("real_copy:", real_copy)

    nested = [["a", "b", "c"], [1, 2, 3]]
    print("nested[0][1] =", nested[0][1])


def fibonacci_demo(limit=50):
    print(f"\n-- fibonacci up to {limit} --")
    a, b = 0, 1
    while a < limit:
        print(a, end=",")
        a, b = b, a + b
    print()  # final newline


if __name__ == "__main__":
    numbers_demo()
    strings_demo()
    lists_demo()
    fibonacci_demo()
