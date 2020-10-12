---
title: "Other Comprehensions"
date: 2019-03-10T19:13:39-07:00
draft: false
weight: 3
---

### Dictionary Comprehensions

Dictionary comprehensions are a quick and easy way of assembling dictionaries in Python. They work just like list comprehensions, and look almost the same. They use curly braces instead of square brackets, and they contain two variables (for `key` and `value`), separated by a colon.

For example, to assemble a `dict` in which the keys are numbers between 0 and 10, and the values are the same number squared, we could do:

```python
>>> squares = {num:num * num for num in range(10)}
>>> print(squares)
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```

Or we could use f-strings to assemble a `dict` to keep game scores:

```python
>>> scores = {f"player-{num}":0 for num in range(0, 5)}
>>> print(scores)
{'player-0': 0, 'player-1': 0, 'player-2': 0, 'player-3': 0, 'player-4': 0}
```

In the above example, the f-string gets turned into the `dict` keys (`player-0`, etc.) and each value is set to 0. You can also operate on tuples for setting keys and values. For example, we'll use a list comprehension to create a list of tuples, then turn the tuples into `dict` keys and values:

```python
>>> my_list = [(f"player-{num}", num * 2) for num in range(0, 5)]
>>> print(my_list)
[('player-0', 0), ('player-1', 2), ('player-2', 4), ('player-3', 6), ('player-4', 8)]
>>> scores = {key:value for (key, value) in my_list}
>>> print(scores)
{'player-0': 0, 'player-1': 2, 'player-2': 4, 'player-3': 6, 'player-4': 8}
```

### Set Comprehensions

Set comprehensions are another great operation in Python - they look like a cross between `list` and `dict` comprehensions, and they create `set` objects.

For example:
```python
>>> my_set = {num for num in [1, 2, 1, 0, 3]}
>>> print(my_set)
{0, 1, 2, 3}
```

Notice that instead of returning the same list of numbers (as `num for num` would have done in a list comprehension), you instead get a `set` (note the curly braces) of unique numbers from the list (you only get one `1`).


### Generator Expressions

Generator expressions are a little more advanced. A generator is a type of iterable object - like a list, you can iterate through each element - however, unlike a list, generators evaluate elements on demand, instead of assembling them all at once.

A generator comprehension looks just like a list comprehension, except we use parenthesis instead of brackets. For example, to get a list of the square of every even number between 0 and 10, we could do:

```python
# List comprehension
>>> list_comp = [x ** 2 for x in range(10) if x % 2 == 0]
>>> print(list_comp)
[0, 4, 16, 36, 64]

# Generator expression
>>> gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)
>>> print(gen_exp)
<generator object <genexpr> at 0x10d48cc00>
>>> for num in gen_exp:
...     print(num)
...
0
4
16
36
64
```

Generator comprehensions can be beneficial in circumstances where you want to iterate over very large lists without storing the entire list in memory. For example, if you tried to assemble a list of every number between 0 and 10 ** 8 (10 to the 8th power), Python will try to assemble the entire list in memory. Using the `timeit` library to create this list only once, we can see how long this takes:

```python
>>> list_comp = "[num for num in range(0, 10 ** 8)]"
>>> import timeit
>>> timeit.timeit(list_comp, number=1)
7.578090285999998
# Over 7 seconds just to assemble one huge list
# Let's do the same with a generator comprehension instead:
>>> gen_comp = "(num for num in range(0, 10 ** 8))"
>>> timeit.timeit(gen_comp, number=1)
9.919999996554907e-06
>>> timeit.timeit(gen_comp, number=10000000)
7.211805443999992
```

As you can see, assembling the generator is almost instantaneous, in fact we can run the generator expression over 10 million times in less time than it takes to assemble the full list once, and the generator will take far less memory.