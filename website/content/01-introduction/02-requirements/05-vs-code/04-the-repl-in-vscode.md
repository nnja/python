---
title: "Using The REPL"
date: 2019-02-10T18:11:15-08:00
draft: false
weight: 4
---

## The REPL

REPL stands for Read, Evaluate, Print, Loop. The REPL is how you interact with the Python Interpreter.

Unlike running a file containing Python code, in the REPL you can type commands and instantly see the output printed out. You can also use the REPL to print out help for methods and objects in Python, list out what methods are available, and much more.

## Open The REPL

To start the REPL in VS code, open the command palette and search for and select "Start REPL". The advantage to starting the REPL from inside VS Code is that it respects the environment you already set up, that is the version of Python you chose earlier.

![Start REPL](/01-introduction/02-requirements/05-vs-code/images/repl-start.png?classes=shadow,border)

Note: If you'd like to start the REPL from the command line outside of the editor, type `python` in your shell,

Running this command should bring up a new pane at the bottom of your editor that you can type into. A great feature of the REPL is that we can instantly see the result of commands being run.

![REPL](/01-introduction/02-requirements/05-vs-code/images/repl.png?classes=shadow,border)

{{% notice note %}}
Note, in the REPL three arrows >>> indicate a line of input given at the prompt.
If you see these arrows in example code, don't copy them into your own REPL.
Later, when we run out Python code from files, you will no longer see the triple arrows.
{{% /notice %}}

Let's get familiar with the REPL.

- `#` - comments start with `#`. They will be ignored.
- `>>>` - this is the prompt. In example code, lines starting with `>>>` means they are **input**
- lines that don't start with either of these are **output** that was produced by running input from the prompt

 by typing these line of code at the `>>>` prompt, and press enter after each line.

```python
# My REPL. Don't copy the >>> symbols, that means the code was entered
# into the prompt.
#
# If the line does not start with >>>, that means it is output,
# not input
>>> name = "Nina"
>>> name
'Nina'
```

In the REPL, we can see the value of any variable just by entering it into the prompt.

You can copy and paste code into the REPL, even multiple lines of code at once. Copy the three lines below and paste them into your REPL. What's the result?

```python
x = 5
y = 33.5
x * y
```

{{%expand "See the result." %}}
```python
>>> x = 5
>>> y = 33.5
>>> x * y
167.5
```
{{% /expand%}}

The REPL allows us to gather information in real time about our Python program, which makes it a great learning tool.

## Using `type()`, `dir()`, and `help()`

We can use three very useful methods in the REPL to help us understand our Python programs.

Pass in an object into the `type()` Use type to find the type of an object in Python.

{{% notice info %}}
If you're not sure what a variable or an object is, don't worry. We'll cover it later in the day.
{{% /notice %}}

For example, in the REPL, let's make a new variable `name`, and check its `type`.

```python
>>> name = "Nina"
>>> type(name)
<class 'str'>
```

We'll see that the type is `str`, Python's version of a string. Now that we know this object's type, we can
pass the type into other methods.

The first one is `dir()` which stands for directory. If we check the directory of `str` (notice, no quotes here)) in the REPL, we'll see all the methods available on strings in Python. Don't worry about these for now, we'll use them later in the day.

```Python
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

The next useful method is `help()`. You can pass a type, method, or other object to help to instantly see available documentation about the method, the parameters it expects, and what it returns.

Let's try this in the REPL, and look up the documentation for the `isupper` method in String. We access it with the period symbol (`.`). This is called dot-notation.

```python
>>> help(str.isupper)
```

Will show:

```text
isupper(self, /)
    Return True if the string is an uppercase string, False otherwise.

    A string is uppercase if all cased characters in the string are uppercase and
    there is at least one cased character in the string.
```

{{% notice note %}}
Press the 'q' key to exit this screen.
{{% /notice %}}

Keep note of these three helpful methods, and don't be afraid to use them throughout class.

## Why Use The REPL?

In this class, we'll be working with a mix of the REPL and running code in files, like we'll see in the next section. You'll want to store code for reuse in files, while you can consider the REPL more of a scratch area. It's the place where you can instantly play around and try out Python code. The REPL is a handy tool for both beginner and advanced Python programmers.

We'll use the REPL for the majority of Day 1, and move on to running Python files in Day 2.