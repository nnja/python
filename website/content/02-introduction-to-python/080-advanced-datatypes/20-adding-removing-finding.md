+++
title = "Lists, Part 2"
date = 2019-03-03T17:22:06-08:00
weight = 20
draft = false
+++

### Adding, Removing, Changing, and Finding Items in `list`s cheat sheet

| action                                           	| method                                	| returns           	| possible errors                            	|
|--------------------------------------------------	|---------------------------------------	|-------------------	|--------------------------------------------	|
| check length                                     	| `len(my_list)`                        	| `int`             	|                                            	|
| **add:** to the end                              	| `my_list.append(item)`                	| -                 	|                                            	|
| **insert:** at position                          	| `my_list.insert(pos, item)`           	| -                 	|                                            	|
| **update:** at position                          	| `my_list[pos] = item`          	| -        -         	| `IndexError` if `pos` is >= `len(my_list)`                                          	|
| **extend:** add items from another list          	| `my_list.extend(other_list)`          	| -                 	|                                            	|
| is item in list?                                 	| `item in my_list`                     	| `True` or `False` 	|                                            	|
| **index** of item                                	| `my_list.index(item)`                 	| `int`             	| `ValueError` if `item` is not in `my_list` 	|
| **count** of item                                	| `my_list.count(item)`                 	| `int`             	|                                            	|
| **remove** an item                               	| `my_list.remove(item)`                	| -                 	| `ValueError` if `item` not in `my_list`    	|
| **remove** the last item, or an item at an index 	| `my_list.pop()` or `my_list.pop(pos)` 	| `item`            	| `IndexError` if `pos` >= `len(my_list)`    	|


#### Checking Length

Before we add or remove items, it's usually a good idea to check a list's length. We do that with the `len` built in function. We can even use the `len` built in function to check the lengths of other types, like strings.

Let's see it in action on a names `list` with two items, and a name `str`ing with four characters.

```python
>>> len(names)
2
>>> name = "Nina"
>>> len(name)
4
```

### Adding Items

Let's start with a list of two names.

```python
>>> names = ["Nina", "Max"]
```

##### `my_list.append(item)` adds to the end of `my_list`

We can use `my_list.append(item)` to add an additional item to the end of the list.

```python
>>> names.append("John")
>>> names
['Nina', 'Max', 'John']
```

##### `my_list.insert(pos, item)` inserts an item into `my_list` at the given position

Use `my_list.insert(pos, item)` to insert items in an arbitrary position in the list. If the position is 0, we'll insert at the beginning of the list.

```python
>>> names.insert(0, "Rose")
>>> names
['Rose', 'Nina', 'Max', 'John']
```

You can call `dir()` on our names list to verify that it's actually of type `list`. If you forget which order insert is called in, don't forget you can always use the `help()` function on the REPL. **Remember: Press `q` to quit the help screen.** Let's try it now:

```python
>>> type(names)
<class 'list'>
>>> help(names.insert)

Help on method_descriptor:

insert(self, index, object, /)
    Insert object before index.
```

You can also call help on `names.insert`. Because `names` is already of type `list`, it achieves the same result.

##### `my_list.extend(other_list)` adds all the contents of `other_list` to `my_list`

```python
>>> names = ["Nina", "Max"]
>>> colors = ["Red", "Blue"]
>>> names
['Nina', 'Max']
>>> names.extend(colors)
>>> names
['Nina', 'Max', 'Red', 'Blue']
```

### Looking for Items

Looking for items in a list is *slow*. Each item needs to be checked in order to find a match.

This doesn't matter much when you're just getting started, unless your data set is large, or if you're building high-performance systems. If you want to quickly search for an item, you'll need to use a `set` or a `dict`ionary instead.

There are a few ways to determine if an item is in the list, and at which position. Let's try this on our list of names.

```python
names = ["Nina", "Max", "Phillip", "Nina"]
```

##### Use the `in` keyword to determine if an item is present or not.

```python
>>> "Nina" in names
True
>>> "Rose" in names
False
```

##### Use the `my_list.index(item)` method to find the **first** index of a potential match.

Notice that only the *first* index of the string `"Nina"` is returned. We'll learn more about what an index is in the next chapter.

{{% notice info %}}
If the item we're looking for *is not* in the list, Python will throw a `ValueError`.
{{% /notice %}}

You'll learn how to deal with exceptions later. For now, you can use the `in` operator to check if an item is present in the list before finding its index.

```python
>>> names.index("Nina")
0
>>> names.index("Rose")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'Rose' is not in list
```

##### Use the `my_list.count(item)` method to find out how many times an item appears in a list.

```python
>>> names.count("Nina")
2
>>> names.count("Rose")
0
```

### Updating Items

To update items in a list, use the *position* of the item you'd like to change using square bracket `[]` syntax. Like: `my_list[pos] = new_item`

For example:

```python
>>> names = ["Nina", "Max"]
>>> names[0] = "Rose"
>>> names
['Rose', 'Max']
```

Or, when used with `my_list.index(item)`:

```python
>>> names = ["Nina", "Max"]
>>> pos = names.index("Max")
>>> names[pos] = "Rose"
>>> names
['Nina', 'Rose']
```

{{% notice info %}}
You'll see a `IndexError: list assignment index out of range` if you try to update an item in a position that doesn't exist, that is *if the position is greater than or equal to `>=` the length of the list*.
{{% /notice %}}

```python
>>> names = ["Nina", "Max"]
>>> len(names)
2
>>> names[2] = "Rose"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
```

### Removing Items

There are a few ways to remove items from a list.

##### Use `my_list.remove(item)` to remove the *first* instance of the item

Be careful. `remove()` only removes the first instance of the item from the list, which isn't always what we want to do.

```python
>>> names = ["Nina", "Max", "Rose"]
>>> names.remove("Nina")
>>> names
['Max', 'Rose']
>>>
>>>
>>> names = ["Nina", "Max", "Nina"]
>>> names.remove("Nina")
>>> names
['Max', 'Nina']
```

{{% notice info %}}
If we try to remove an item that's not in the list, we'll get a `ValueError: list.remove(x): x not in list`.
{{% /notice %}}

```python
>>> names = ["Nina"]
>>> names.remove("Max")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
```

##### Use `my_list.pop()` to remove the last item, or `my_list.pop(index)` to remove the item at that index

Using `pop()` will also **return** the item that was in that position. That's useful if we want to save the item.

```python
>>> names = ["Nina", "Max", "Rose"]
>>> names.pop()
'Rose'
>>> names
['Nina', 'Max']
>>> names.pop(1)
'Max'
>>> names
['Nina']
```

{{% notice info %}}
If we try to pop an item from an index that is longer than or equal to the length of the list, we'll get an `IndexError: pop index out of range`.
{{% /notice %}}

```python
>>> names = ["Nina"]
>>> len(names)
1
>>> names.pop(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop index out of range
```
