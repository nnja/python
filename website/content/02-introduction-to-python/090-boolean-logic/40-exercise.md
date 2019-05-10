---
title: "Practice"
date: 2019-03-03T00:00:00-08:00
draft: false
weight: 40
pre: "<b>⭐️ </b>"
---

## Boolean Logic

### Comparisons

Let's practice using our comparison operators. Remember:

|Operator|Means|
|---|---|
|`<`|less-than|
|`<=`|less-than-or-equal-to|
|`>`|greater-than|
|`>=`|greater-than-or-equal-to|
|`==`|equals|
|`!=`|not-equals|

Remember, the first six operators test the object's *value*. `is` and `is not` test whether two objects are the same thing. This is useful for singletons, such as `None` or `False`. We won't be using them much in this intro course, but feel free to play with them.

```python
>>> 10 > 5
>>> 5 > 10
>>> 10 > 10
>>> 10 >= 10
>>> 5 < 10
>>> 5 < 5
>>> 5 <= 5
>>> 5 == 5
>>> 5 != 10
```

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> 10 > 5
True
>>> 5 > 10
False
>>> 10 > 10
False
>>> 10 >= 10
True
>>> 5 < 10
True
>>> 5 < 5
False
>>> 5 <= 5
True
>>> 5 == 5
True
>>> 5 != 10
True
```

{{% /expand %}}

### Truthiness

Different languages have different ideas of what is "truthy" and "falsy." In Python, all objects can be tested for truth, and an object is considered True unless except under certain circumstances that we talked about earlier in the chapter. Remember that checking if an object is "equal" to another object doesn't necessarily mean the same thing. An object is considered "truthy" if it satisfies the check performed by `if` or `while` statements.

Let's try a few of these out:

```python
>>> 5 == True
>>> # The number 5 does not equal True, but...
>>> if 5:
...     print("The number 5 is truthy!")
...
>>> # The number 5 is truthy for an if test!
```

True and False can also be represented by 1 and 0
```python
>>> 1 == True
>>> 0 == False
```

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> 5 == True
False
>>> # The number 5 does not equal True, but...
>>> if 5:
...     print("The number 5 is truthy!")
...
The number 5 is truthy!
>>> # The number 5 is truthy for an if test!
```

```python
>>> 1 == True
True
>>> 0 == False
True
```
{{% /expand %}}

### Boolean Operators

Python also supports boolean operators, although they're a little different than the comparison operators. Remember that `or` and `and` return one of their operands, rather than `True` or `False`.

|Operation|Result|
|---|---|
|`x or y`|if x is false, then y, else x|
|`x and y`|if x is false, then x, else y|
|`not x`|if x is false, then `True`, else `False`|

```python
>>> True or False
>>> [] or [1, 2, 3]
>>> "Hello" or None
```

```python
>>> True and False
>>> 5 and 0
>>> [1] and [1, 2, 3]
>>> "Hello" and None
```

```python
# Of course, you can use `and` and `or` aren't limited to two operands
>>> a = False
>>> b = False
>>> c = False
>>> a or b or c
>>> b = True
>>> a or b or c

>>> a and b and c
>>> a = True
>>> c = True
>>> a and b and c
```

{{%expand "Here's what you should have seen in your REPL:" %}}
```python
>>> True or False
True
>>> [] or [1, 2, 3]
[1, 2, 3]
>>> "Hello" or None
'Hello'
```

```python
>>> True and False
False
>>> 5 and 0
0
>>> [1] and [1, 2, 3]
[1, 2, 3]
>>> "Hello" and None
>>> # No output, since the result was None
```

```python
>>> a = False
>>> b = False
>>> c = False
>>> a or b or c
False
>>> b = True
>>> a or b or c
True

>>> a and b and c
False
>>> a = True
>>> c = True
>>> a and b and c
True
```

{{% /expand %}}
