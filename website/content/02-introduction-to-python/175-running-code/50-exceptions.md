+++
title = "Exceptions and Tracebacks"
date = 2019-01-25T15:03:40-06:00
weight = 50
draft = false
+++

We talked about how to read the traceback you see if an error occurs in a Python program earlier in the day, but let's talk about what we can do about it.

### Uncaught Exceptions Exit Our Program

Let's make a file called `exceptions.py`:

```python
# this will throw an exception!
int("a")

print("End of the program.")
```

And run it:
```bash
(env) $ python exceptions.py

Traceback (most recent call last):
  File "/Users/nina/projects/2019-fem-python/python/content/02-introduction-to-python/175-running-code/code/exceptions.py", line 2, in <module>
    int("a")
ValueError: invalid literal for int() with base 10: 'a'
```

We'll see that "Reached end of the program" was never printed out.

{{% notice warning %}}
If we're running our Python code from a file, an uncaught exception will quit the program.
{{% /notice %}}

### Using `try` and `except` to catch Exceptions

In order to prevent our program from exiting, we'll need to *catch* the Exception with a `try` `except` block. The anatomy of a `try` `except` block:

```text
try:
    <code to try>
except ExceptionClass:
    <code to run if an exception happens>
```

In order to write a `try` `except` block, we'll need to know the class name of the Exception we'd like to catch. Luckily, the name is printed right there, in the traceback!

Let's update `exceptions.py`

```python
try:
    int("a")
except ValueError:
    print("Oops, couldn't convert that value into an int!")

print("Reached end of the program.")
```

And the output:

```bash
(env) $ python exceptions.py
Oops, couldn't convert that value into an int!
Reached end of the program.
```

{{% notice tip %}}
You want to catch Exceptions that are as specific as possible.
{{% /notice %}}

### Using `as` to Access The Exception

You can optionally assign a label to the exception, and the exception will be assigned to the variable you specified, so you can look at it's message, or examine it in other ways with `except <ExceptionClass> as <variable_name>`.

Using this syntax, `variable_name` can be anything. In this case, I picked `error`, but you'll commonly see `e` used for this purpose in Python programs.

Let's update `exceptions.py` one more time:

```python
try:
    int("a")
except ValueError as error:
    print(f"Something went wrong. Message: {error}")

print("Reached end of the program.")
```

If we run this code, we'll see:

```bash
(env) $ python exceptions.py
Something went wrong. Message: invalid literal for int() with base 10: 'a'
Reached end of the program.
```

{{% notice note %}}
This example just scratches the surface. We'll cover Exceptions in much more detail in Day 2.
{{% /notice %}}

### Anatomy of a Traceback

When running our code from Python files, we'll need to look at your tracebacks a little more carefully.

{{% notice tip %}}
Remember, to understand tracebacks, read them from bottom to top.
{{% /notice %}}

When we ran our first example, we saw:

```text
Traceback (most recent call last):
  File "/Users/nina/projects/2019-fem-python/python/content/02-introduction-to-python/175-running-code/code/exceptions.py", line 2, in <module>
    int("a")
ValueError: invalid literal for int() with base 10: 'a'
```

If we start reading from the bottom up, we'll notice a lot of useful information.

1. First, we'll see the exception that was thrown, along with its class `ValueError`.
2. Next, we'll see the code that caused the Exception.
3. One line up from that, we'll see the path and the file the exception originated in, as well as the **line number** to look on.