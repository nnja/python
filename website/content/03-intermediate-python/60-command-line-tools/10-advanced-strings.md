---
title: "Advanced Strings"
date: 2019-02-10T18:17:18-08:00
draft: false
weight: 1
---

## Advanced f-strings

### Decimal Formatting

Formatting decimal or floating point numbers with f-strings is easy - you can pass in both a field width and a precision. The format is {value:width.precision}. Let's format pi (3.1415926) to two decimal places - we'll set the width to 1 because we don't need padding, and the precision to 3, giving us the one number to the left of the decimal and the two numbers to the right:

```python
>>> print(f"Pi to two decimal places is {3.1415926:1.3}")
Pi to two decimal places is 3.14

# We'll break it out into variables to make it clearer:
>>> value = 3.1415926
>>> width = 1
>>> precision = 3
>>> print(f"Pi to two decimal places is: {value:{width}.{precision}}")
Pi to two decimal places is: 3.14

# Let's change the width to 10
>>> value = 3.1415926
>>> width = 10
>>> precision = 3
>>> print(f"Pi to two decimal places is: {value:{width}.{precision}}")
Pi to two decimal places is:       3.14
```

Note how the second one is padded with extra spaces - the number is four characters long (including the period), so the formatter added six extra spaces to equal the total width of 10.


### Multiline Strings

Sometimes it's easier to break up large statements into multiple lines. Just prepend every line with `f`:

```python
>>> name = 'Nina'
>>> pi = 3.14
>>> food = 'pie'
>>> message = (
...     f"Hello, my name is {name}. "
...     f"I can calculate pi to two places: {pi:4.3}. "
...     f"But I would rather be eating {food}."
... )
>>> print(message)
Hello, my name is Nina. I can calculate pi to two places: 3.14. But I would rather be eating pie.
```

### Trimming a string

Python strings have some very useful functions for trimming whitespace. `strip()` returns a new string after removing any leading and trailing whitespace. `rstrip()` and does the same but only removes trailing whitespace, and `lstrip()` only trims leading whitespace. We'll print our string inside `><` characters to make it clear:

```python
>>> my_string = "   Hello World!   "
>>> print(f">{my_string.lstrip()}<")
>Hello World!   <
>>> print(f">{my_string.rstrip()}<")
>   Hello World!<
>>> print(f">{my_string.strip()}<")
>Hello World!<
```

Note the different spaces inside of the brackets. These functions also accept an optional argument of characters to remove. Let's remove all leading or trailing commas:

```python
>>> my_string = "Hello World!,,,"
>>> print(my_string.strip(","))
Hello World!
```


### Replacing Characters

Strings have a useful function for replacing characters - just call `replace()` on any string and pass in what you want replace, and what you want to replace it with:

```python
>>> my_string = "Hello, world!"
>>> my_string.replace("world", "Nina")
'Hello, Nina!'
```

### `str.format()` and `%` formatting

Python has two older methods for string formatting that you'll probably come across at some point. `str.format()` is the more verbose older cousin to `f-strings` - variables appear in brackets in the string but must be passed in to the `format()` call. For example:

```python
>>> name = "Nina"
>>> print("Hello, my name is {name}".format(name=name))
Hello, my name is Nina
```

Note that the variable name inside the string is local to the string - it must be assigned to an outside variable inside the `format()` call, hence `.format(name=name)`.

%-formatting is a much older method of string interpolating and isn't used much anymore. It's very similar to the methods used in C/C++. Here, we'll use `%s` as our placeholder for a string, and pass the `name` variable in to the formatter by placing it after the `%` symbol.

```python
>>> name = "Nina"
>>> print("Hello, my name is %s" % name)
Hello, my name is Nina
```