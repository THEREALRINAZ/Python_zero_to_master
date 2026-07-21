# Day 02 Notes — Numbers, Strings, and Lists

## 1. Comments

Comments start with `#` and run to the end of the line. They can sit on their own line or trail after code, but a `#` inside a string literal is just a regular character, not a comment:

```python
# this is a comment
spam = 1  # this one trails after code
text = "# this is not a comment, it's just text in quotes"
```

## 2. Numbers

The interpreter works like a calculator: type an expression, get a value back.

- `int` — whole numbers (`2`, `4`, `20`)
- `float` — numbers with a fractional part (`5.0`, `1.6`)

Standard operators: `+`, `-`, `*`, `/` for arithmetic, and `()` for grouping.

Regular division (`/`) **always** returns a float, even if the result is a whole number. For integer-style division there are two separate operators:

```python
17 / 3    # -> 5.666666666666667  (true division, always float)
17 // 3   # -> 5                  (floor division, drops the remainder)
17 % 3    # -> 2                  (modulo, gives the remainder)
```

Powers use `**`:

```python
5 ** 2   # -> 25
2 ** 7   # -> 128
```

Mixing an `int` and a `float` in an operation converts the result to `float`.

**A neat interactive-mode detail:** the last printed result is automatically stored in a special variable `_`, so you can chain calculations without retyping the previous result:

```python
tax = 12.5 / 100
price = 100.50
price * tax     # -> 12.5625
price + _       # uses the previous result -> 113.0625
```

This only applies in interactive mode, and `_` should be treated as read-only — assigning to it manually just creates a normal variable that happens to be named `_`, overriding the automatic behavior.

## 3. Strings

Strings (`str`) can use single quotes, double quotes, or triple quotes — single and double quotes behave identically:

```python
'hello'
"hello"
```

To include a quote character inside a string, either escape it with `\` or switch to the other quote style:

```python
'it\'s fine'
"it's fine"      # simpler — no escaping needed
```

**Raw strings** (prefix `r`) turn off escape-sequence interpretation, which is useful for things like Windows file paths:

```python
print('C:\text')     # \t is interpreted as a tab — breaks the path
print(r'C:\text')     # printed exactly as written
```

**Multi-line strings** use triple quotes (`"""..."""` or `'''...'''`) and can span several lines directly.

**Concatenation:**
- `+` joins strings together: `'Py' + 'thon'` → `'Python'`
- `*` repeats a string: `'un' * 3` → `'ununun'`
- Two string *literals* sitting next to each other are joined automatically (useful for breaking up long strings across lines) — but this only works with literals, not variables. Joining a variable with a literal requires `+`.

**Indexing and slicing** — strings are zero-indexed, and negative indices count from the end:

```python
word = 'Python'
word[0]    # -> 'P'
word[-1]   # -> 'n'  (last character)
word[0:2]  # -> 'Py' (slice: start included, end excluded)
word[:2]   # -> 'Py' (omitted start defaults to 0)
word[4:]   # -> 'on' (omitted end defaults to the string's length)
```

Slicing out of bounds doesn't error — it just returns whatever fits.

**Strings are immutable** — you can't reassign a character at a given position. Any "change" actually builds a new string:

```python
word[0] = 'J'        # raises TypeError
'J' + word[1:]        # -> 'Jython' (this is how you actually do it)
```

`len()` returns a string's length.

## 4. Lists

Lists group values together, written with square brackets: `[1, 4, 9, 16, 25]`. Items can be mixed types, though usually they're the same type.

Like strings, lists support indexing and slicing — but unlike strings, **lists are mutable**:

```python
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64          # fix a wrong value in place
cubes.append(216)      # add a new item at the end
```

**The aliasing gotcha:** assigning a list to a new variable does *not* copy it — both variables point at the same underlying list. Changing one changes the other:

```python
rgb = ["Red", "Green", "Blue"]
rgba = rgb              # rgba is NOT a copy — same list, two names
rgba.append("Alpha")
rgb                      # -> ["Red", "Green", "Blue", "Alpha"]  (changed too!)
```

To actually get an independent copy, slice the whole thing:

```python
new_list = rgba[:]   # shallow copy — a genuinely separate list
```

Slice assignment can replace, insert, or delete multiple items at once, and can even resize or clear the list entirely:

```python
letters = ['a', 'b', 'c', 'd', 'e']
letters[1:3] = ['B', 'C']   # replace a range
letters[1:3] = []            # delete a range
letters[:] = []               # clear everything
```

Lists can also be nested (a list containing other lists), and you chain indices to reach inner items: `x[0][1]`.

## 5. First Real Program Logic

**Multiple assignment** evaluates the whole right-hand side first, then assigns:

```python
a, b = 0, 1
```

**`while` loops** run as long as a condition stays true. Comparison operators are the usual set: `<`, `>`, `==`, `<=`, `>=`, `!=`.

**Indentation is how Python groups statements** — there's no `{}` block syntax. Every line inside the same block must be indented consistently.

Putting it together — a classic Fibonacci-sequence generator:

```python
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b
```

**`print()`** inserts a space between multiple arguments and prints strings without their surrounding quotes. The `end` keyword controls what gets printed after the value instead of the default newline:

```python
a, b = 0, 1
while a < 50:
    print(a, end=',')
    a, b = b, a + b
# prints: 0,1,1,2,3,5,8,13,21,34,
```

## Summary

Today was about the raw materials — numbers, text, and lists — plus the two mechanics (`while` + indentation) that turn isolated expressions into an actual running program. The aliasing behavior of lists is the one detail worth remembering hardest; it's a quiet source of bugs if you assume assignment always copies.
