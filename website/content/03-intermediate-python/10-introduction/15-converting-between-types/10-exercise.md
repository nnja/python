---
title: "Practice"
date: 2019-03-08T00:00:00-08:00
draft: false
weight: 10
pre: "<b>⭐️ </b>"
---

## Converting Between Types

Converting between types in Python is one of the most powerful language features.

You can quickly convert between strings, numbers, and various data-types to supercharge quickly solving problems.
You can even use powerful data structures like sets to your advantage.

## Converting Between Numbers and Strings

Converting between numbers and strings is easy with `str()` and `int()`:

```python
>>> my_string = str(100)
>>> my_string
>>> type(my_string)
>>> my_int = int(my_string)
>>> my_int
>>> type(my_int)
```

You can also use `float()` to convert strings into floating point numbers:

```python
>>> float("3.1415")
3.1415
```

Bonus tip: `int()` works great for converting floats as well, as long as you don't care about the mantissa (the part after the decimal point):

```python
>>> int(3.1415)
```

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> my_string = str(100)
>>> my_string
'100'
>>> type(my_string)
<class 'str'>
>>> my_int = int(my_string)
>>> my_int
100
>>> type(my_int)
<class 'int'>
```

```python
>>> float("3.1415")
3.1415
```

```python
>>> int(3.1415)
3
```
{{%/expand%}}

## Converting Between Lists and Strings

A `str`ing can be considered as just a list of characters, so converting back and forth is easy:

```python
>>> my_list = list("hello")
>>> my_list
>>> str(my_list)
```

Oops, that wasn't quite what we wanted. Running any object through `str()` will usually return a literal string of that object. What we want is to *join* the elements of the list (into a string). We can do that using string's built-in `join()` method. In this case, we'll use an empty string:

```python
>>> ''.join(my_list)
# Note: we can use any string we want to join the characters!
>>> ','.join(my_list)
>>> '-'.join(my_list)
```

Another common way of converting a string into a list is with the string's `split()` method. This is useful for lightweight parsing of, for example, CSV (comma separated value) data.

```python
>>> my_string = "the,quick,brown,fox"
>>> my_string.split(",")
```

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> my_list = list("hello")
>>> my_list
['h', 'e', 'l', 'l', 'o']
>>> str(my_list)
"['h', 'e', 'l', 'l', 'o']"
```

```python
>>> ''.join(my_list)
'hello'

>>> ','.join(my_list)
'h,e,l,l,o'
>>> '-'.join(my_list)
'h-e-l-l-o'
```

```python
>>> my_string = "the,quick,brown,fox"
>>> my_string.split(",")
['the', 'quick', 'brown', 'fox']
```

{{%/expand%}}
