---
title: "while loops"
date: 2019-02-10T18:22:01-08:00
draft: false
weight: 30
---

`while` loops are a special type of loop in Python. Instead of running just once when a condition is met, like an `if` statement, they run **forever** until a condition is *no longer* met.

`while` loops usually need to be accompanied by an always changing sentinel value.

```python
>>> counter = 0
>>> max = 4
>>>
>>> while counter < max:
...     print(f"The count is: {counter}")
...     counter = counter + 1
...
The count is: 0
The count is: 1
The count is: 2
The count is: 3
```

{{% notice warning %}}
Our loop will run forever if we forget to *update* the sentinel value. **Press Ctrl-C to exit the infinite loop.**
{{% /notice %}}


```python
# Warning: don't copy and paste this example.

>>> counter = 0
>>> max = 4

>>> while counter < max:
...     print(f"The count is: {counter}")
...
# What happens if we don't update counter?
The count is: 0
The count is: 0
The count is: 0
The count is: 0
# An infinite loop repeated until we hit Ctrl-C
The count ^CTraceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt
```