---
title: "Practice"
date: 2019-03-09T00:00:00-08:00
draft: false
weight: 10
pre: "<b>⭐️ </b>"
---

### Comprehensions

Let's practice our comprehensions. Create a list of only odd numbers between 0 and 100 using a list comprehension. Then, use a comprehension to create a dictionary where the keys are the even numbers from your list, and the values are random integers between 0 and 100 (hint: try `random.randint(min, max)`). Finally, use a comprehension to create a set of every unique value from the above dictionary.

```python
>>> my_list = [num for num in range(0, 100) if num % 2 == 0]
>>> print(my_list)

>>> import random
>>> my_dict = {num:random.randint(0, 100) for num in my_list}
>>> print(my_dict)

>>> my_set = {num for num in my_dict.values()}
>>> print(my_set)
```

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> my_list = [num for num in range(0, 100) if num % 2 == 0]
>>> print(my_list)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

>>> import random
>>> my_dict = {num:random.randint(0, 100) for num in my_list}
>>> print(my_dict)
{0: 37, 2: 84, 4: 56, 6: 45, 8: 63, 10: 57, 12: 39, 14: 25, 16: 18, 18: 10, 20: 52, 22: 95, 24: 93, 26: 89, 28: 96, 30: 77, 32: 16, 34: 91, 36: 19, 38: 14, 40: 92, 42: 35, 44: 85, 46: 86, 48: 44, 50: 32, 52: 38, 54: 34, 56: 23, 58: 71, 60: 37, 62: 100, 64: 98, 66: 15, 68: 84, 70: 40, 72: 47, 74: 30, 76: 42, 78: 36, 80: 62, 82: 49, 84: 11, 86: 58, 88: 60, 90: 6, 92: 41, 94: 28, 96: 16, 98: 93}

>>> my_set = {num for num in my_dict.values()}
>>> print(my_set)
{6, 10, 11, 14, 15, 16, 18, 19, 23, 25, 28, 30, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 45, 47, 49, 52, 56, 57, 58, 60, 62, 63, 71, 77, 84, 85, 86, 89, 91, 92, 93, 95, 96, 98, 100}
```

{{%/expand%}}


### Slicing

You know how to create a list of even or odd numbers with a list comprehension. Make a list of numbers between 0 and 100, then try making a list of even numbers between 30 and 70, by taking a slice from the first list. Then, make a new list in the reverse order.

```python
>>> my_list = [num for num in range(0, 100)]
>>> my_slice = my_list[30:70:2]
>>> print(my_slice)
>>> my_backwards_slice = my_slice[::-1]
>>> print(my_backwards_slice)
```

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> my_list = [num for num in range(0, 100)]
>>> my_slice = my_list[30:70:2]
>>> print(my_slice)
[30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68]
>>> my_backwards_slice = my_slice[::-1]
>>> print(my_backwards_slice)
[68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30]
```

{{%/expand%}}


### `zip`

Make a list of all the names you can think of, called "names". Make a second list of numbers, called "scores", using a list comprehension and `random.randint(min, max)` as before. Use the first list in your comprehension to make it the same length. Then, use `zip()` to output a simple scoreboard of one score per name.

```python
>>> names = ["Nina", "Max", "Floyd", "Lloyd"]
>>> scores = [random.randint(0, 100) for name in names]
>>> scores
[41, 38, 96, 81]
>>> for name, score in zip(names, scores):
...     print(f"{name} got a score of {score}")
...
```

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> names = ["Nina", "Max", "Floyd", "Lloyd"]
>>> scores = [random.randint(0, 100) for name in names]
>>> scores
[41, 38, 96, 81]
>>> for name, score in zip(names, scores):
...     print(f"{name} got a score of {score}")
...
Nina got a score of 41
Max got a score of 38
Floyd got a score of 96
Lloyd got a score of 81
```

{{%/expand%}}
