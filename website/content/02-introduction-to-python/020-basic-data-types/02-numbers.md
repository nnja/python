---
title: "Numbers"
date: 2019-02-03T23:14:25-08:00
draft: false
weight: 2
---

First, open up the REPL.

{{% notice tip %}}
Remember, you'll learn best if you type along with me.
{{% /notice %}}

There are three different types of numbers in Python: `int` for Integer, Float, and Complex.

```python
# These are all integers
x = 4
y = -193394
z = 0
```

```python
# These are all floats
x = 5.0
y = -3983.2
z = 0.
```

```python
# This is a complex number
x = 42j
```

In Python, Integers and other simple data types are just objects under the hood. That means that you can create new ones by calling methods. You can provide either a number, or a string. This will come in handy later on in the course.

```python
x = int(4)
y = int('4')
z = float(5.0)
```

Python also provides a `decimal` library, which has certain benefits over the `float` datatype. For more information, refer to the [Python documentation](https://docs.python.org/3/library/decimal.html).

## Mathematical Operations

Numbers can be added together. If you add a `float` and an `int`, the resulting type will be a `float`.

If you divide two `int`s (integers), the result will be of type `float`.

## Boolean Types

In Python, Booleans are of type `bool`. Surprisingly, the boolean types `True` and `False` are also numbers under the hood.

* `True` is `1` under the hood.
* `False` is `0` under the hood.

That means you can do silly things, like add two Boolean numbers together, but I'll cover why this is a useful Python feature later in the course.