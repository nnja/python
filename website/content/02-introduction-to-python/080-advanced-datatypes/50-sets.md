---
title: "Sets"
date: 2019-02-10T18:20:42-08:00
draft: false
weight: 50
---

Sets are a datatype that allows you to store other **immutable** types in an unsorted way. An item can only be contained in a set once. There are no duplicates allowed. The benefits of a set are: very fast membership testing along with being able to use powerful set operations, like `union`, `difference`, and `intersection`.

### `set` cheat sheet

| type               	| `set`                                                                                                                         	|
|--------------------	|-------------------------------------------------------------------------------------------------------------------------------	|
| use                	| Used for storing immutable data types uniquely. Easy to compare the items in `set`s.                                          	|
| creation           	| `set()` for an empty set (`{}` makes an empty `dict`) and `{1, 2, 3}` for a set with items in it                              	|
| search methods     	| `item in my_set`                                                                                                              	|
| search speed       	| Searching for an item in a large set is very fast.                                                                            	|
| common methods     	| `my_set.add(item)`, `my_set.discard(item)` to remove the item if it's present, `my_set.update(other_set)` 	|
| order preserved?   	| **No**. Items *can't* be accessed by index.                                                                                   	|
| mutable?           	| **Yes**. Can add to or remove from `set`s.                                                                                    	|
| in-place sortable? 	| **No**, because items aren't ordered.                                                                                                                        	|
### Examples

#### Empty `set`s

Let's create our first few sets.

The first thing we might try to do is create an empty set with `{}`, but we'll come across a hurdle.

```python
>>> my_new_set = {}
>>> type(my_new_set)
<class 'dict'>
>>> my_set = set()
>>> type(my_set)
<class 'set'>
```

{{% notice info %}}
You can't create an empty `set` with `{}`. That creates a `dict`. Create an empty set with `set()` instead.
{{% /notice %}}

{{% notice tip %}}
While you're learning Python, it's useful to use `type()`, `dir()` and `help()` as often as possible.
{{% /notice %}}

#### `set`s with items

Now, let's make a new set with some items in it, and test out important set concepts.

#### `set`s can't contain duplicate values

```python
>>> names = {"Nina", "Max", "Nina"}
>>> names
{'Max', 'Nina'}
>>> len(names)
2
```

#### `set`s can't contain mutable types

The way that `set`s allow you to quickly check if an item is contained in them or not is with an algorithm called a hash. I won't cover the details, but an algorithm is a way of representing an immutable data type with a unique numerical representation. In Python, there's a built-in `hash()` function.

The `hash()` function only works on immutable data types. That means, data types where the contents can't be changed after creation.

```python
>>> hash("Nina")
3509074130763756174
>>> hash([])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

{{% notice info %}}
You'll see a `TypeError: unhashable type: 'list'` if you try to add a mutable data type (like a `list`) to a set.
{{% /notice %}}

If you try to add a mutable data type (like a `list`) to a set, you'll see the same `TypeError`, complaining about an `unhashable type`.

```python
>>> {"Nina"}
{'Nina'}
>>> {[]}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

#### `set`s can be used to de-duplicate the items in a list

Tip: *If you don't care about order*, you can quickly de-duplicate the items in a `list` by passing the `list` into the `set` constructor.

```python
>>> colors = ["Red", "Yellow", "Red", "Green", "Green", "Green"]
>>> set(colors)
{'Red', 'Green', 'Yellow'}
```

#### `set`s don't have an order

Sets don't have an order. That means that when you print them, the items won't be displayed in the order they were entered in the list.

```python
>>> my_set = {1, "a", 2, "b", "cat"}
>>> my_set
{1, 2, 'cat', 'a', 'b'}
```

It also means that you *can't* access items in the `set` by position in subscript `[]` notation.

```python
>>> my_set = {"Red", "Green", "Blue"}
>>> my_set[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support indexing
```

{{% notice info %}}
You'll see `TypeError: 'set' object does not support indexing` if you try to access the items in a `set` by index with `my_set[pos]`
{{% /notice %}}

Tip: If your set contains items of the same type, and you want to sort the items, you'll need to convert the `set` to a `list` first. Or, you can use the built-in `sorted(sequence)` method, which will do the conversion for you.

```python
>>> my_set = {"a", "b", "cat", "dog", "red"}
>>> my_set
{'b', 'red', 'a', 'cat', 'dog'}
>>> sorted(my_set)
['a', 'b', 'cat', 'dog', 'red']
```

#### adding to and removing from `set`s

Since a set has no order, we can't add or remove items to it by index. We need to call the operations with the item itself.

##### Add items to a set with `my_set.add(item)`.

```python
>>> colors = {"Red", "Green", "Blue"}
>>> colors.add("Orange")
>>> colors
{'Orange', 'Green', 'Blue', 'Red'}
```

##### Remove items with `my_set.discard(item)`

You can remove an item from a `set` if it's present with `my_set.discard(item)`. If the set doesn't contain the item, no error occurs.

```python
>>> colors = {"Red", "Green", "Blue"}
>>> colors.discard("Green")
>>> colors
{'Blue', 'Red'}
>>> colors.discard("Green")
>>> colors
{'Blue', 'Red'}
```

You can also remove items from a `set` with `my_set.remove(item)`, which will raise a `KeyError` if the item doesn't exist.


##### Update a set with another sequence using `my_set.update(sequence)`

You can update a `set` by passing in another sequence, meaning another `set`, `list`, or `tuple`.

```python
>>> colors = {"Red", "Green"}
>>> numbers = {1, 3, 5}
>>> colors.update(numbers)
>>> colors
{1, 3, 'Red', 5, 'Green'}
```

{{% notice info %}}
Be careful passing in a `str`ing to `my_set.update(sequence)`. That's because a `str`ing is *also* a sequence. It's a sequence of characters.
{{% /notice %}}

```python
>>> numbers = {1, 3, 5}
>>> numbers.update("hello")
>>> numbers
{1, 3, 'h', 5, 'o', 'e', 'l'}
```

Your set will update with each character of the `str`ing, which was probably not your intended result.

### `set` operations

`sets` allow quick and easy operations to compare items between two sets.

#### `set` operations cheat sheet

 method operation    	| symbol operation 	| result                                                                        	|
|---------------------	|------------------	|-------------------------------------------------------------------------------	|
| `s.union(t)`        	| <code>s &#124; t</code> | creates a new set with all the items **from both `s` and `t`**             |
| `s.intersection(t)` 	| `s & t`          	| creates a new set containing *only* items that are **both in `s` and in `t`** 	|
| `s.difference(t)`    	| `s ^ t`          	| creates a new set containing items that are **not in both `s` and in `t`**                        	|

#### examples

Let's see it in action.

We have two sets, `rainbow_colors`, which contain the colors of the rainbow, and `favorite_colors`, which contain my favorite colors.

```python
>>> rainbow_colors = {"Red", "Orange", "Yellow", "Green", "Blue", "Violet"}
>>> favorite_colors = {"Blue", "Pink", "Black"}
```

First, let's combine the sets and create a new `set` that contains all of the items from `rainbow_colors` and `favorite_colors` using the union operation. You can use the `my_set.union(other_set)` method, or you can just use the symbol for union `|=` from the table above.

```python
>>> rainbow_colors | favorite_colors
{'Orange', 'Red', 'Yellow', 'Green', 'Violet', 'Blue', 'Black', 'Pink'}
```

Next, let's find the intersection. We'll create a new `set` with *only* the items in both `set`s.

```python
>>> rainbow_colors & favorite_colors
{'Blue'}
```

Lastly, We can also find the difference. Create a new set with the items that are in in one, but not the other. We'll see that `"Blue"` is missing from the list.

```python
>>> rainbow_colors ^ favorite_colors
{'Orange', 'Red', 'Yellow', 'Green', 'Violet', 'Black', 'Pink'}
```

There are other useful operations available on `set`s, such as checking if one set is a subset, a superset, and more, but I don't have time to cover them all. Python also has a `frozenset` type, if you need the functionality of a `set` in an immutable package (meaning that the contents can't be changed after creation).

Find out more by reading the [documentation](https://docs.python.org/3/library/stdtypes.html#set), or calling `help()` on `set`.
