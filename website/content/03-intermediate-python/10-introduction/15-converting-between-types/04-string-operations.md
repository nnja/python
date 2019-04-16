---
title: "String Operations"
date: 2019-02-10T18:30:43-08:00
draft: false
weight: 4
---

### Split and Join

Strings have two functions for splitting and joining - `split()` and `join()`. Calling `split()` on a string will split the string into a list, creating a new element for every instance of the character(s) you pass in. `join()` accepts a list of strings, and uses the string you call it on to join the list together into one string. For example:

```python
>>> my_data = "this,is,comma,separated,data"
>>> my_data = my_data.split(",")
>>> print(my_data)
['this', 'is', 'comma', 'separated', 'data']

>>> ":".join(my_data)
'this:is:comma:separated:data'

>>> ", ".join(my_data)
'this, is, comma, separated, data'
```