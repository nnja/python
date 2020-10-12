---
title: "Printing Tips"
date: 2019-02-10T18:13:59-08:00
draft: false
weight: 20
---

One of the nice things about the REPL is we can quickly and easily see the contents of our variables, just by typing their name and pressing enter. Unfortunately, running code from Python files doesn't do quite the same thing.

In a file named `name.py`:

```python
# file name.py
name = "Nina"
name
```

Output:

```bash
(env) $ python name.py
```

*Notice, there was no output.*

Now, in a file named `print_name.py`:
```python
# file print_name.py
name = "Nina"
print(name)
```

Output:
```bash
(env) $ python name.py
Nina
```

Hooray! Now we see some output. 🎉

{{% notice tip %}}
If you want to see any output from your Python programs, you'll need to use `print()`.
{{% /notice %}}

### Debugging Your Code With `print()`

As your Python programs become more complicated, you'll want to do some basic debugging to figure out what's going on under the hood. For beginners, using `print()` is a great way to accomplish that goal.

{{% notice note %}}
If you write Python code on a team or plan on sharing it, it's a good idea to *remove* your debugging `print()`s before you share your code with others.
{{% /notice %}}

In a Python file named `mystery.py`:

```python
def mystery():
    num = 10 * 3

    if num == 10:
        print("Num was equal to 10")
        num = num * 10
    if num == 20:
        print("Num was equal to 20")
        num = num * 20
    if num == 30:
        print("Num was equal to 30")
        num = num * 30

    print(f"Value of returned num is: {num}")
    return num

mystery()
```

We'll see the output:

```python
Num was equal to 30
Value of returned num is: 900
```

{{% notice tip %}}
Tip: As you continue your Python journey, try using a debugger, like the built-in `pdb` instead of the `print()` function to really dive into what your code is doing under the hood.
{{% /notice %}}


### Output Formatting Tips

If your Python program will have terminal output, you can use these tips to make it a little nicer.

#### Use new lines and tabs


Use control characters in your string to change how your output is represented.

* `\n` for new line
* `\t` for tab

In `formatting_example.py`:

```python
# Use \n to add a new line, before, in the middle of, or after a string.
print("\nExtra New Line Before")
print("One Print\nTwo New Lines!")
print("Extra New Line After\n")

# Use \t to add a tab.
print("\t Here's some tabbed output.")

# Or, combine both!
print("\nOne Print\n\tOne Tab")
```

Output running: `python3 formatting_example.py`.

```text
Extra New Line Before
One Print
Two New Lines!
Extra New Line After

         Here's some tabbed output.

One Print
        One Tab
```

#### Pretty Printing with `pprint`

When printing large data structures like long lists or big dictionaries, they come out on one line. It's a bit hard to read.

If you want a little bit of extra formatting, like having each element of a long list on a new line, you can use the included `pprint` module (stands for pretty print) in your files or in the REPL.

```python
>>> long_list = list(range(23))

>>> print(long_list)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

>>> from pprint import pprint
>>> pprint(long_list)
[0,
 1,
 2,
 3,
 4,
 5,
 6,
 7,
 8,
 9,
 10,
 11,
 12,
 13,
 14,
 15,
 16,
 17,
 18,
 19,
 20,
 21,
 22]
```

{{% notice tip %}}
This will become more useful as your Python programs become more complex.
{{% /notice %}}