---
title: "and, or, not"
date: 2019-02-10T18:17:45-08:00
draft: false
weight: 30
---

`and`, `or`, and `not` are the three basic types of boolean operators that are present in math, programming, and database logic.

In other programming languages, you might have seen the concept of `and` represented with `&&`, `or`, represented with `||`, and `not` represented by `!`. The Python language is instead focused on readability. So we'll use the english `and` instead of trying to remember fancy symbols. Python still uses the `&`, `|` and `!` expressions, but they're used for bitwise operations.

You can use them to compare one (or more expressions) and determine if they evaluate to `True` or `False`.

Thankfully, you don't have to be a computer scientist to understand them if you use this handy table.

### `and`, `or`, `not` Cheat Sheet

|Operation|Result|
|---|---|
|`a or b`|if a is False, then b, else a|
|`a and b`|if a is False, then a, else b|
|`not a`|if a is false, then `True`, else `False`|


### `and`

<!--
| a       	| b       	| a `and` b  	|
|---------	|---------	|------------	|
| `True`  	| `True`  	| **`True`** 	|
| `True`  	| False 	| False    	|
| False 	| `True`  	| False    	|
| False 	| False 	| False    	|
-->

{{% notice note %}}
For `a and b`, if a is false, a is returned. Otherwise b is returned.
*If `a and b` are both `bool`ean values, the expression evaluates to`True` if both a and b are `True`.*
{{% /notice %}}

```python
>>> a = True    # a is True
>>> b = True
>>> a and b     # True is returned. (value of b)
True

>>> a = False   # a is False
>>> b = True
>>> a and b     # False is returned. (value of a)
False

>>> a = False   # a is False
>>> b = False
>>> a and b     # False is returned. (value of a)
False
```

Notice what happens when do the same thing to values that have a "truthiness" to them.

```python
>>> bool(0) # Verify that zero is "falsey"
False
>>> bool(1) # Verify that one is "truthy"
True
>>> 0 and 1 # 0 is False. 0 is returned.
0
```

### `or`

<!--
| a       	| b       	| a `or` b   	|
|---------	|---------	|------------	|
| `True`  	| `True`  	| **`True`** 	|
| `True`  	| False 	| **`True`** 	|
| False 	| `True`  	| **`True`** 	|
| False 	| False 	| False    	|
-->

{{% notice note %}}
For `a or b`, if a is false, b is returned. If a is true, a is returned.
*`a or b` evaluates to `True` if either (or both) of the expressions are true.*
{{% /notice %}}

```python
>>> a = True    # a is true
>>> b = True
>>> a or b      # True is returned (value of a)
True

>>> a = False   # a is false
>>> b = True
>>> a or b      # True is returned (value of b)
True

>>> 0 or 1      # 0 is false. Return 1.
1
```

### `not`

| a       	| `not` a    	|
|---------	|------------	|
| true  	| False    	|
| false 	| **`True`** 	|


{{% notice note %}}
`not a` reverses the `bool`ean value of `a`. If it *was* true, it will return `False`. If it was false, it will return `True`.
{{% /notice %}}

```python
>>> a = True
>>> not a  # not returns the opposite. True -> False
False

>>> a = False
>>> not a  # not returns the opposite. False -> True
True
```

And again, with numbers. Remember, zero is considered `False`, any other number is considered `True`.

```python
>>> bool(1)
True
>>> not 1
False
>>> bool(0)
False
>>> not 0
True
```

### In Combination

When combining multiple boolean operators, you can add optional parenthesis for readability.

```python
>>> a = True
>>> b = True
>>> c = False

>>> a and (b or c)
True
```

You can combine multiple operators to test complex assumptions. For example, to return `True` only if *both* values are `False`, we can use the `not` negation operation on the result of an `or`.

```python
>>> a = False
>>> b = False

>>> a or b  # False because both are False.
False

>>> not (a or b)  # True - checking if both are False.
True
```

### With "truthiness"

Remember, we learned that some values in Python are *falsey* like the number zero, and some are *truthy* like any number *expect* for zero.

It's a little counter intuitive, but when we compare values other than `bool`eans, our code behaves a little differently.

|Operation|Result|
|---|---|
|`x or y`|if x is false, then y, else x|
|`x and y`|if x is false, then x, else y|

Let's see it in action. First, lets test our assumptions again.

```python
>>> bool(0)     # Truthiness of 0 is False
False

>>> bool(1)     # Truthiness of 1 is True
True

>>> bool(None)  # Truthiness of None type is False
False

>>> 1 or 0      # Returns 1, the True value
1

>>> 1 and 0     # Returns 0, the False value
0

>>> 0 or None   # Neither are True. Returns nothing (None)
```