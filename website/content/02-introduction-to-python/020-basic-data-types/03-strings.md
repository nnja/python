---
title: "Strings"
date: 2019-02-03T23:14:35-08:00
draft: false
weight: 3
---

#### Representing Strings

Strings in Python can be enclosed either with single quotes like `'hello'` or double quotes, like `"hello"`.

Strings can also be **concatenated** (added together) using the `+` operator to combine an arbitrary number of Strings. For example:

<pre><code class="plaintext">1334</code></pre>

```python
salutation = "Hello "
name = "Nina"
greeting = salutation + name
# The value of greeting will be "Hello Nina"
```

To use the same type of quote within a string, that quote needs to be **escaped** with a `\` - backwards slash.

```python
greeting = 'Hello, it\'s Nina'
```

Alternately, mixed quotes can be present in a Python string without escaping.

```python
# Notice that the single quote ' is surrounded by
# double quotes, ""
greeting = "Hello, it's Nina"
```

Long multi-line strings can be represented in between `"""` (triple quotes), but the whitespace will be part of the string.

```python
long_greeting = """
                Greetings and salutations, dear Nina.
                I'm superfluous with my words,
                and require more space to say Hello!"
                """
```

#### Printing Strings

Strings can be printed out using the `print()` function in Python. While you're working the REPL, you'll see that variables are displayed for you. When you move on to writing standalone Python programs, that will no longer be the case.

To use the `print()` function, call it with a regular or formatted string.

```python
>>> print("Hello")
Hello
>>> name = "Nina"
>>> print(name)
Nina
```

#### String Formatting

There are several types of string formatting in Python.

If you're using Python 3.7 and above (remember to check with `python --version` on the command line) you can use my favorite type of string formatting, and the one I'll be using for the course called f-strings.

```python
>>> name = "Nina"
>>> greeting = f"Hello, {name}"

>>> print(greeting)
Hello, Nina
```

f-strings allow you to simply and easily reference variables in your code, and as a bonus, they're *much* faster.