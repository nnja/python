---
title: "Practice"
date: 2019-02-04T15:28:32-08:00
draft: false
weight: 10
pre: "<b>⭐️ </b>"
---

## Basic Data Types, Strings and Numbers

### Types

List the type of the following variables using the `type()` function.

```python
>>> x = 42
>>> y = 3 / 4
>>> z = int('7')
>>> a = float(5)
>>> name = "Nina"
```

### Numbers

Calculate the amount of rent you pay daily, by taking your monthly rent and diving it by 30.

```python
>>> rent = 480
>>> per_day = rent / 30
>>> print(per_day)
16.0
```

### Strings

Try printing some things to your REPL:

```python
>>> print("Hello world")
Hello world
>>> name = "Nina"
>>> print("My name is", name)
My name is Nina
```

There are three different ways to format strings in Python3. You may run into %-formatting and `str.format()` in older code. These are still common in Python but no longer recommended, due to readability concerns.

```python
>>> name = "Nina"
>>> print("Hello, my name is %s" % name)
Hello, my name is Nina
```

The current recommended way to format string is with f-Strings. f-Strings are much more readable and easier to maintain than the previous methods. With f-Strings, your string is prepended with the letter `f` and your variables or expressions to interpret are placed in `{brackets}`.

```python
>>> name = "Nina"
>>> print(f"Hello, my name is {name} and I pay ${rent / 30} in rent per day")
Hello, my name is Nina and I pay $16.0 in rent per day
```

### Helper Functions

Python has a few built-in functions to help you if you get stuck. `type()` tells you what an object's type is, for example a string (`str`) or integer (`int`). `dir()` returns a list of valid attributes for an object, so you can quickly see what variables an object has or what functions you can call on it. `help()` brings up helpful documentation on any object. You can also type `help()` on its own to bring an interactive help console.

```python
>>> x = 42
>>> y = 3 / 4
>>> name = "Nina"
>>> type(x)
<class 'int'>
>>> type(y)
<class 'float'>
>>> type(name)
<class 'str'>
```