"""
Day 01 — Examples
Run this file a few different ways to see how the interpreter behaves.

1) Normal script run:
       python3 examples.py foo bar
2) As a module:
       python3 -m examples foo bar   (run from inside this folder)
3) Directly via -c (paste the print_argv function body):
       python3 -c "import sys; print(sys.argv)"
"""

import sys


def print_argv():
    """Show exactly what sys.argv looks like for this run."""
    print(f"Script name (argv[0]): {sys.argv[0]}")
    print(f"Extra arguments: {sys.argv[1:]}")
    print(f"Total argv list: {sys.argv}")


def demo_interactive_style_block():
    """
    This mirrors the kind of multi-line block you'd type at the >>> / ... prompts
    in interactive mode — here it's just a normal function body.
    """
    the_world_is_flat = True
    if the_world_is_flat:
        print("Be careful not to fall off!")
    else:
        print("No edge to worry about.")


if __name__ == "__main__":
    print("--- sys.argv demo ---")
    print_argv()

    print("\n--- interactive-style block demo ---")
    demo_interactive_style_block()

    print("\nTry running this file with extra arguments, e.g.:")
    print("    python3 examples.py hello world")
