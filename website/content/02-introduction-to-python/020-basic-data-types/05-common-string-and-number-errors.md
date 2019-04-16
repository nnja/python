---
title: "Common Mistakes"
date: 2019-02-10T18:33:43-08:00
draft: false
weight: 5
---

There are a few common errors that you'll encounter when working with Strings and numbers. Remember, in Python program errors are called Exceptions. By going over what they are, you'll be able to recognize them immediately.

### Scenario 1: Mismatched string quotes

{{% notice info %}}
Mismatched string quotes will result in a `SyntaxError`
{{% /notice %}}

When we try to start a String with one type of quote, and end with another, we'll see a syntax error.

For example, starting the string Hello with a double quote, and ending in a single quote, like this:

#### Input: **"**Hello**'**

For example, in the REPL:

```python
>>> name = 'Hello"
  File "<stdin>", line 1
    name = "Hello'
                 ^
SyntaxError: EOL while scanning string literal
```

**Solution:** use matching quote types for defining your strings. Either single quotes `'Hello'` or double quotes `"Hello"`.

### Scenario 2: Trying to print a String and a number with concatenation using the "+" symbol.

{{% notice info %}}
Trying to add or concatenate a String and a number will result in a `TypeError`
{{% /notice %}}

If you add try to add (or concatenate) a String and a number, you'll get an error saying that adding the two types together isn't possible.

#### Input: 3 + "Three"

In the REPL:
```python
>>> print(3 + " Three")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

**Solutions:**

There are two possible solutions here, for two different scenarios.

In the first scenario, you'd like to add a number to a string via concatenation. In order to do that, you must first convert the number to a string via the `str()` method.

In the REPL:
```python
>>> my_num = 3
>>> print(str(my_num) + " Three")
3 Three
```

In the second scenario, you'd like to a convert a number that's contained in a string (ex: `"3"`) into an Integer, so you can use it like any other number. In this case, you'd like to convert it to an Integer, with the `int()` method.

In the REPL:
```python
>>> str_num = "3"
>>> print(int(str_num) + 5)
8
```