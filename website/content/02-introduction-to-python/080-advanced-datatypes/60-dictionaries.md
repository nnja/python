---
title: "Dictionaries"
date: 2019-02-10T18:20:37-08:00
draft: false
weight: 60
---

Dictionaries are a useful type that allow us to store our data in key, value pairs. Dictionaries themselves are **mutable**, *but*, dictionary keys can only be **immutable** types.

We use dictionaries when we want to be able to quickly access additional data associated with a particular key. A great practical application for dictionaries is memoization. Let's say you want to save computing power, and store the result for a function called with particular arguments. The arguments could be the key, with the result stored as the value. Next time someone calls your function, you can check your dictionary to see if the answer is pre-computed.

Looking for a key in a large dictionary is extremely fast. Unlike lists, we don't have to check every item for a match.

### `dict`ionary cheat sheet

| type               	| `dict`                                                                                                                                             	|
|--------------------	|----------------------------------------------------------------------------------------------------------------------------------------------------	|
| use                	| Use for storing data in key, value pairs. Keys used must be **immutable** data types.                                                              	|
| creation           	| `{}` or `dict()` for an empty `dict`. `{1: "one", 2: "two"}` for a `dict` with items.                                                              	|
| search methods     	| `key in my_dict`                                                                                                                                   	|
| search speed       	| Searching for a key in a large dictionary is fast.                                                                                                 	|
| common methods     	| `my_dict[key]` to get the value by `key`, and throw a `KeyError` if `key` is not in the dictionary. Use `my_dict.get(key)` to fail silently if `key` is not in `my_dict`. `my_dict.items()` for all key, value pairs, `my_dict.keys()` for all keys, and `my_dict.values()` for all values. 	|
| order preserved?   	| **Sort of**. As of Python 3.6 a `dict` is sorted by insertion order. Items *can't* be accessed by index, only by key.                              	|
| mutable?           	| **Yes**. Can add or remove keys from `dict`s.                                                                                                      	|
| in-place sortable? 	| **No**. `dict`s don't have an index, only keys.                                                                                                    	|

### Examples

#### Empty `dict`s

We already learned one of the methods of creating an empty `dict` when we tried (and failed) to create an empty set with `{}`. The other way is to use the `dict()` method.

```python
>>> my_dict = {}
>>> type(my_dict)
<class 'dict'>

>>> my_dict = dict()
>>> type(my_dict)
<class 'dict'>
```

#### Creating `dict`s with items

If we want to create `dict`s with items in them, we need to pass in key, value pairs. A `dict` is declared with curly braces `{}`, followed by a key and a value, separated with a colon `:`. Multiple key and value pairs are separated with commas `,`.


We can call familiar methods on our dictionary, like finding out how many key / value pairs it contains with the built-in `len(my_dict)` method.

```python
>>> nums = {1: "one", 2: "two", 3: "three"}

>>> len(nums)
3
```

#### Side note: What can be used as keys?

Any type of object, mutable or immutable, can be used as a value but just like `set`s, `dict`ionaries can only use immutable types as keys. That means you can use `int`, `str`, or even `tuple` as a key, but **not** a `set`, `list`, or other `dict`ionary.

The follow is OK:

```python
>>> my_dict = {1: 1}
>>> my_dict = {1: []}
```

{{% notice info %}}
You'll see a `TypeError: unhashable type: 'list'` if you try to use a mutable type, like a `list` as a `dict`ionary key.
{{% /notice %}}

```python
>>> my_dict = {[]: 1}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

#### Accessing

Our `dict` contains `key`, `value` pairs. Because a `dict`ionary isn't ordered, we *can't access the items in it by position*. Instead, to access the items in it, we use square-bracket `my_dict[key]` notation, similar to how we access items in a list with square bracket notation containing the position.

```python
>>> nums = {1: "one", 2: "two", 3: "three"}
>>> nums[1]
'one'
>>> nums[2]
'two'
```

Q: What happens when we try to access a key in a `dict`ionary with square bracket notation, but the key isn't present?

{{% notice info %}}
We'll get a `KeyError: key` if we try to access `my_dict[key]` with square bracket notation, but `key` isn't in the dictionary.
{{% /notice %}}

```python
>>> nums = {1: "one", 2: "two", 3: "three"}
>>> nums[4]

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 4
```

One way to get around this is to use the `my_dict.get(key)` method. Using this method, if the key isn't present, no error is thrown, and no value (aka the `None` type) is returned.

```python
>>> nums = {1: "one", 2: "two", 3: "three"}
>>> nums.get(4)

>>> result = nums.get(4)
>>> type(result)
<class 'NoneType'>
```

If we want to provide a *default value* if the key is missing, we also pass an *optional* argument to the `my_dict.get(key)` method like so: `my_dict.get(key, default_val)`

```python
>>> nums = {1: "one", 2: "two", 3: "three"}
>>> nums.get(4, "default")
'default'
```

#### Adding, Removing

To add a new key value pair to the dictionary, you'll use square-bracket notation.

If you try to put a key into a dictionary that's already there, you'll just end up replacing it. To avoid subtle bugs, you can check if a particular key is in a dictionary with the `in` keyword. We'll cover that technique in Chapter 6 - Control Statements and Looping.

```python
>>> nums = {1: "one", 2: "two", 3: "three"}
>>> nums[8] = "eight"

>>> nums
{1: 'one', 2: 'two', 3: 'three', 8: 'eight'}

>>> nums[8] = "oops, overwritten"
>>> nums
{1: 'one', 2: 'two', 3: 'three', 8: 'oops, overwritten'}
>>> 8 in nums
True
```

#### Updating

Just like with `list`s an `set`s, you can update the items in a dictionary with the items from another dictionary.

```python
>>> colors = {"r": "Red", "g": "Green"}
>>> numbers = {1: "one", 2: "two"}
>>> colors.update(numbers)
>>> colors
{'r': 'Red', 'g': 'Green', 1: 'one', 2: 'two'}
```

### Complex Dictionaries

One incredibly useful scenario for dictionaries is storing the values in a `list` or other sequence. Going into too much detail is outside of the scope of the class, but I'll show you a quick example:

```python
>>> colors = {"Green": ["Spinach"]}
>>> colors
{'Green': ['Spinach']}
>>> colors["Green"].append("Apples")
>>> colors
{'Green': ['Spinach', 'Apples']}
```

### Working with `items`, `keys`, and `values`

There are three useful methods you need to remember about `dict`ionary access:

1. `my_dict.keys()`
2. `my_dict.values()`
3. `my_dict.items()`

#### 1. `my_dict.keys()` Getting all the keys in a dictionary

```python
>>> nums = {1: 'one', 2: 'two', 3: 'three', 8: 'eight'}
>>> nums.keys()
dict_keys([1, 2, 3, 8])
```

#### 2. `my_dict.values()` Getting all the values in a dictionary.

```python
>>> nums = {1: 'one', 2: 'two', 3: 'three', 8: 'eight'}
>>> nums.values()
dict_values(['one', 'two', 'three', 'eight'])
```

#### 3. `my_dict.items()` Getting all the items (key, value pairs) in a dictionary

Notice that `my_dict.items()` returns a type that looks like a list. It contains two-item `tuple`s containing the key, value pairs.

```python
>>> nums = {1: 'one', 2: 'two', 3: 'three', 8: 'eight'}
>>> nums.items()
dict_items([(1, 'one'), (2, 'two'), (3, 'three'), (8, 'eight')])
```
