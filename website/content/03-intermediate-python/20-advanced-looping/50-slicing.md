---
title: "Slicing"
date: 2019-03-10T19:13:03-07:00
draft: false
weight: 5
---

Slicing is a easy way to create sub-lists from larger lists. If you remember back to our exercise on data types, we can use a slice to obtain a subset of items from a `list`. Remember that a string is just a list of characters. For example:

```python
>>> my_string = "Hello, world!"
>>> my_string[7:12] # from 7 to 12
'world'
```

### Lopsided Slicing

You can also leave out one of the numbers in the slice. Leaving out the first number is equivalent to using a zero - you can think of this as "from the beginning." Leaving out the last number is equivalent to using the length of the list you're slicing - you can think of this as "until the end." For example:

```python
>>> my_string = "Hello, world!"
>>> my_string[:5] # from zero to 5
'Hello'
>>> my_string[7:] # from 7 to the end
'world!'
```

You can also leave out both sides of the slice! You can think of this as "from the beginning, until the end." Why? This is an easy way to copy a list!

```python
>>> my_new_string = my_string[:]
>>> my_new_string
'Hello, world!'
```

### Negative Indexing

You aren't limited to positive numbers for your slicing, either. A negative number on the left side will wrap around to the other side of your list. A negative number on the right side is equivalent to the length of the list minus your number. For example:

```python
>>> my_string = "Hello, world!"
>>> my_string[-6:] # from the end - 6 to the end
'world!'
>>> my_string[-10:-4] # from the end - 10 to the end - 4
'lo, wo'
```

You can also use just a single negative number to get an item counting *backwards* from the end of a `list`. For example, to get the last item from a list:

```python
>>> my_list = [1, 3, 3, 7]
>>> my_list[-1]
7
```

### Stride or Step

Python slices also have a *third*, optional argument, called "step" or "stride", separated by a second colon. This lets you skip elements of a list or even reverse them. For example:

```python
>>> my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> my_list[::2] # move forward by 2, or skip every other index
[0, 2, 4, 6, 8]
>>> my_list[::-1] # move backward by 1, and easy way to reverse a list
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> my_list[1:7:2] # get every other index between 1 and 7
[1, 3, 5]
```

{{% notice note %}}
You can use a slice to get a subset of items from any data type that maintains an order, such as a `list` or `tuple`, but not from any non-ordered data types, such as `dict` or `set`.
{{% /notice %}}