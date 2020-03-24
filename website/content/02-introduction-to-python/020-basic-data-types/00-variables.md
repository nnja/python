---
title: "Variables and Types"
date: 2019-02-03T23:26:13-08:00
draft: false
weight: 1
---

### Naming Variables

Python variables can't start with a number. In general, they're named all lower case, separated by underscores. Unlike other languages, that name their variables with camelCase.

You don't want to name your variables the same as the *types* that we'll be working with. For example **don't** name your variables `int`, `list`, `dict`. Etc.

### Open The REPL

Learn about variables by typing along in the Python REPL with me.

{{% notice tip %}}
Open the REPL from VS Code by opening the command palette (ctrl + shift + P on Windows, or cmd + shift + P on Mac) and selecting Python: Start REPL
{{% /notice %}}

Any Python code that starts with the `>>>` symbols indicates that it was typed into a REPL.

You can then use ctrl + ` (backtick) to open and close the VS Code terminal on Mac, or ctrl + ' (single quote) on Windows. You won't lose your work in the REPL unless you close VS Code.

{{% notice info %}}
If you'd like to save the contents of your REPL as class goes on, you can right click, select all, and paste it into a new file.
{{% /notice %}}

## Variables

Variables in Python allow us to store information and give it a label that we can use to retrieve that information later. We can use variables to store numbers, strings (a sequence of characters), or even more complex data types like lists and dictionaries.

We assign _values_ to _variables_ by putting the _value_ to the right of an equal sign.

Because Python is a *dynamic* language, we don't need to declare the type of the variables before we store data in them.

That means that this is valid Python code:

```python
>>> x = 42
```

Unlike typed languages, the type of what's contained in Python variables can change at any time.

For example, the below is perfectly valid Python code:

```python
>>> x = 42
>>> x = "hello"
```

Here, the value of the variable `x` changed from a number to a string.

When creating variables, there are a few best practices you should follow.

#### Naming Variables

Convention says that variables should be named in lowercase, with whole words separated by underscores.

{{% notice note %}}
If you want to learn more about Python naming conventions look at [PEP8](https://www.python.org/dev/peps/pep-0008/#naming-conventions) during a break.
{{% /notice %}}

Because Python is a dynamic language and you don't have type hints to explain what's stored inside a variable while reading code, you should do your best naming your variables to describe what is stored inside of them.

It's ok to be _verbose_. For example, `n` is a poor variable name, while `numbers` is a better one. If you're storing a collection of items, name your variable as a plural.

{{% notice note %}}
Learn more about great naming practices for dynamic types by watching this 30-minute [talk by Brandon Rhodes](https://www.youtube.com/watch?v=YklKUuDpX5c).
{{% /notice %}}

#### Naming Gotchas

There are some things that you can't name your variables, such as `and`, `if`, `True`, or `False`. That's because Python uses these names for program control structure.

You can't start your variable name with a digit, although your variable name can end in a digit. Your variable name can't contain special characters, such as `!`,  `@`,  `#`, `$`,  `%` and more.

{{% notice warning %}}
💣 Python will let you override built-in methods and types without a warning so don't name your Python variables things like `list`, `str`, or `int`.
{{% /notice %}}

If you notice your program behaving oddly and you can't find the source of the bug, double check the list of [built-in functions](https://docs.python.org/3/library/functions.html) and [built-in types](https://docs.python.org/3/library/stdtypes.html) to make sure that your variable names don't conflict.

## Types

Python has a very easy way of determining the type of something, with the `type()` function.

```python
>>> num = 42
>>> type(num)
<class 'int'>
```

### No-Value, `None`, or Null Value

There's a special type in Python that signifies no value at all. In other languages, it might be called Null. In Python, it's called `None`.

If you try to examine a variable on the REPL that's been set to `None`, you won't see any output. We'll talk more about the `None` type later in the class.

```python
>>> x = None
>>> x
```
