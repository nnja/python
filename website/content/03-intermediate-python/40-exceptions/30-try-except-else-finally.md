---
title: "Try Except"
date: 2019-03-10T19:15:54-07:00
draft: false
weight: 3
---

Many languages have the concept of the "Try-Catch" block. Python uses four keywords: `try`, `except`, `else`, and `finally`. Code that can possibly throw an exception goes in the `try` block. `except` gets the code that runs if an exception is raised. `else` is an optional block that runs if no exception was raised in the `try` block, and `finally` is an optional block of code that will run last, regardless of if an exception was raised. We'll focus on `try` and `except` for this chapter.

A basic example looks like this:

```python
>>> try:
...     x = int(input("Enter a number: "))
... except ValueError:
...     print("That number was invalid")
```

First, the `try` clause is executed. If no exception occurs, the `except` clause is skipped and execution of the `try` statement is finished. If an exception occurs in the `try` clause, the rest of the clause is skipped. If the exception's type matches the exception named after the `except` keyword, then the `except` clause is executed. If the exception doesn't match, then the exception is *unhandled* and execution stops.


### The `except` Clause

An `except` clause may have multiple exceptions, given as a parenthesized tuple:

```python
try:
    # Code to try

except (RuntimeError, TypeError, NameError):
    # Code to run if one of these exceptions is hit
```

A `try` statement can also have more than one `except` clause:

```python
try:
    # Code to try

except RuntimeError:
    # Code to run if there's a RuntimeError

except TypeError:
    # Code to run if there's a TypeError

except NameError:
    # Code to run if there's a NameError
```

### Finally

Finally, we have `finally`. `finally` is an optional block that runs after `try`, `except`, and `else`, regardless of if an exception is thrown or not. This is good for doing any cleanup that you want to happen, whether or not an exception is thrown.

```python
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print("Goodbye!")
...
Goodbye!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt
```

As you can see, our Goodbye! gets printed just before the unhandled `KeyboardInterrupt` gets propagated up and triggers the traceback.