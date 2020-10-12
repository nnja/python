---
title: "Truthiness"
date: 2019-02-10T18:17:39-08:00
draft: false
weight: 10
---

Evaluating expression to be `True` or `False` will help us control the flow of our program.

### cheat sheet

| type                                        	| truthiness                                                                     	|   	|
|---------------------------------------------	|--------------------------------------------------------------------------------	|---	|
| `int`                                       	| `0` is `False`, all other numbers are `True` (including negative)              	|   	|
| containers - `list`, `tuple`, `set`, `dict` 	| empty container evaluates to `False`, container with items evaluates to `True`) 	|   	|
| `None`                                      	| `False`                                                                        	|   	|

We talked about `boolean` types, `True` and `False` earlier. `True` and `False` are keywords in Python, so make sure you don't name your variables the same thing.

```python
>>> True
True
>>> False
False
```

Sometimes the truth is obvious. For example `3 < 5` is always `True`. Other times, in Python, the truth value might surprise you. Let's review. First, let's start with an expression we know is always `True`.

```python
>>> 3 < 5
True
```

{{% notice tip %}}
Tip: If you want to test your assumptions about an expression that returns `True` or `False`, you can pass it into the constructor for `bool`eans: `bool(expression)`.
{{% /notice %}}

### Numbers

In Python, the integer `0` is always `False`, while every other number, *including negative numbers*, are `True`. In fact, under the hood, `bool`eans inherit from `int`egers.

```python
>>> bool(0)
False
>>> bool(1)
True
>>> bool(-1)
True
```

### Sequences

Empty sequences in Python always evaluate to `False`, **including empty `str`ings.**

```python
>>> bool("")    # String
False
>>> bool([])    # Empty List
False
>>> bool(set()) # Empty Set
False
>>> bool({})    # Empty Dictionary
False
>>> bool(())    # Empty Tuple
False
```

Sequences with at least one value will evaluate to `True`.

```python
>>> bool("Hello")   # String
True
>>> bool([1])       # List
True
>>> bool({1})       # Set
True
>>> bool({1: 1})    # Dictionary
True
>>> bool((1,))      # Tuple
True
```

### `None`

The `None` type in Python represents nothing. No returned value. It shouldn't come as a surprise that the truthiness of `None` is `False`.

```python
>>> bool(None)
False
```

`None` is commonly used as a placeholder to mean *"I haven't set this value yet."* Since empty `str`ings and sequence evaluate to `False`, we need to be very careful when we're checking if a sequence has been *declared* or not, or if it's *empty*.   We'll review this concept again when talking about `if` statements later in the day.

```python
>>> my_name = None
>>> bool(my_name)
False
>>> my_name = ""
>>> bool(my_name)
False

>>> my_list = None
>>> bool(my_list)
False
>>> my_list = []
>>> bool(my_list)
False
```