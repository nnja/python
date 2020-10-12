---
title: "The zip function"
date: 2019-03-03T18:03:03-08:00
draft: false
weight: 7
---

It's often necessary to iterate over multiple lists simultaneously. Suppose we're keeping score of a game and we have two lists, one for names and one for scores:

```python
>>> names = ["Bob", "Alice", "Eve"]
>>> scores = [42, 97, 68]
```

The `zip` function takes any number of iterable arguments and steps through
all of them at the same time until the end of the *shortest* iterable has been reached:

```python
>>> for name, score in zip(names, scores):
>>>     print(f"{name} had a score of {score}.")
...
Bob had a score of 42.
Alice had a score of 97.
Eve had a score of 68.
```

What will the above loop print after removing the last element from `scores`?

```python
>>> scores.pop(-1)
68
>>> for name, score in zip(names, scores):
>>>     print(f"{name} had a score of {score}.")
...
Bob had a score of 42.
Alice had a score of 97.
```

The loop terminates even though there are more values in `names`. Here, Eve isn't included because `scores` only has two elements.

We can also use `zip()` to quickly and easily create a `dict` from two lists. For example:

```python
>>> scores = [42, 97, 68]
>>> score_dict = dict(zip(names, scores))
>>> print(score_dict)
{'Bob': 42, 'Alice': 97, 'Eve': 68}
```