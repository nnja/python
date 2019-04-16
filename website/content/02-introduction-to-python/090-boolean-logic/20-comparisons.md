---
title: "Comparisons"
date: 2019-02-10T18:18:14-08:00
draft: false
weight: 20
---

How can we compare different values with each other?

### Order Comparisons Cheat Sheet

|Operator|Means|
|---|---|
|`<`|less-than|
|`<=`|less-than-or-equal-to|
|`>`|greater-than|
|`>=`|greater-than-or-equal-to|

In Python, comparing numbers is pretty straight forward.

```python
>>> 1 < 10  # 1 is less than 10? True
True
>>> 20 <= 20  # 20 is less than or equal to 20? True
True
>>> 10 > 1  # 10 is greater than 1? True
True
>>> -1 > 1  # -1 is greater than 1? False
False
>>> 30 >= 30  # 30 is greater than or equal to 30? True
True
```

Things get interesting when you try to compare strings. Strings are compared lexicographically. That means by the ASCII value of the character. You don't need to know much about ASCII, besides that capital letters come before lower case ones.

Each character in the two strings is checked one by one, until a character is found that is of a different value. That determines the order. Under the hood, this allows Python to sort strings by comparing them to each other.

```python
>>> "T" < "t"  # Upper case letters are "lower" valued.
True
>>> "a" < "b"
True
>>> "bat" < "cat"
True
```

### Equality Cheat Sheet

|Operator|Means|
|---|---|
|`==`|equals|
|`!=`|not-equals|

The equality operators `val1 == val2` *(`val1` equals `val2`)* and `val1 != val2` *(`val1` doesn't equal `val2`)* compare the contents of two different values and return a `bool`ean.

Equality works like you'd expect it to for simple data types.

```python
>>> a = 1
>>> b = 1
>>> a == b
True
>>> a != b
False

>>> a = "Nina"
>>> b = "Nina"
>>> a == b
True
>>> a != b
False
```

Equality for container types is interesting. Even though `a` and `b` are two different `list`s, their contents are still the same. So compared two lists containing the same values with `==` will return `True`.

```python
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a == b
True
>>> a != b
False
```

### Identity Cheat Sheet

|Operator|Means|
|---|---|
|`is`| *is* the same object in memory? (not equality!)|
|`is not`| *is not* the same object in memory? (not equality!)|

{{% notice note %}}
This is something that trips up Python beginners, so make sure you remember that *equality* (`==`, `!=`) **is not** the same as *identity* (`is`, `not is`).
{{% /notice %}}

The `is` keywords tests if the two compared objects are stored in the same memory location. I won't go into too much detail into why, but remember **not** to use `is` when what you actually want to check for is equality.

```python
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]

>>> a == b  # Testing for equality. a and b contain the same values
True
>>> a is b  # Testing for identity. a and b are NOT the same object.
False
```

{{% notice tip %}}
When you're first starting out, the only place you'll want to use the `is` keyword is to explicitly compare a value to the built-in types of `None`, `True`, or `False`.
{{% /notice %}}

```python
>>> a = True
>>> a is True
True

>>> b = False
>>> b is False
True
>>> b is not True   # Opposite of is b True. aka is b False?
True

>>> c = None
>>> c is None
True
>>> c is not None
False
```