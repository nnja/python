---
title: "Lists, Part 1"
date: 2019-02-10T18:20:32-08:00
draft: false
weight: 10
---

Lists are one of the most powerful data types in Python. Generally, they're container objects used to store related items together.

### `list` cheat sheet

| type             	| `list`                                                                                	|
|------------------	|---------------------------------------------------------------------------------------	|
| use              	| Used for storing similar items, and in cases where items need to be added or removed. 	|
| creation         	| `[]` or `list()` for empty list, or `[1, 2, 3]` for a list with items.                            	|
| search methods   	| `my_list.index(item)` or `item in my_list`                                                                           	|
| search speed     	| Searching in an item in a large list is slow. Each item must be checked.                               	|
| common methods   	| `len(my_list)`, `append(item)` to add, `insert(index, item)` to insert in the middle, `pop()` to remove.         	|
| order preserved? 	| Yes. Items can be accessed by index.                                                  	|
| mutable?         	| Yes                                                                                   	|
| in-place sortable?        	| Yes. `my_list.sort()` will sort the list in-place. `my_list.sort(reverse=True)` will sort the list in-place in *descending* order. `my_list.reverse()` will *reverse the items* in `my_list` in-place.           	|

### In Practice

Let's create a few lists to see how they work.

An empty list can be created in two ways. The first, by calling the `list()` method. More commonly, it's created with two empty brackets `[]`. Don't forget to check the type of the list with the `type` built-in function.

```python
>>> list()
[]
>>> []
[]
>>> type(list())
<class 'list'>
>>> type([])
<class 'list'>
```

Let's create our list with a few items in it. Let's say we want to keep track of a list of names. We add items to our list, and separate them with commas `,`.

```python
>>> names = ["Nina", "Max", "Jane"]
```

We can check its length with the built-in `len()` method, like so:

```python
>>> len(names)
3
```

### Indexes and Indices

Lists retain the order of the items in them. In the next section, you'll learn about some data structures that don't.

In order to *access* items in a list, we'll need to use an *index*. (Multiple indexes are sometimes also called indices). The index for the item you want to access is *an integer* put in *square brackets* after the list.

{{% notice tip %}}
**Indexes start at 0** in Python and most other programming languages.
{{% /notice %}}

```python
>>> names = ["Nina", "Max", "Jane"]
>>> names[0]
'Nina'
>>> names[1]
'Max'
>>> names[2]
'Jane'
```

#### Updating an item in a list

To update a particular item in a `list` use square-bracket notion and assign a new value. `my_list[pos] = new_value`

```python
>>> names = ["Nina", "Max", "Jane"]
>>> names[2] = "Floyd"
>>> names
['Nina', 'Max', 'Floyd']
```

{{% notice info %}}
If you try to access an index that is greater than or equal to (>=) the length of the list, you'll get an `IndexError`.
{{% /notice %}}

```python
>>> names = ["Nina", "Max", "Jane"]
>>> len(names)
3
>>> names[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

#### Formatting

{{% notice tip %}}
We can *optionally* add new lines after the commas. This helps with readability for more complex list items.
{{% /notice %}}

Notice that we can also *optionally* add a trailing comma after the last item. A trailing comma isn't required to create a valid list, but it does help minimize version control differences when working on a Python codebase with a team.

```python
>>> names = [
... "Nina",
... "Max",
... "Jane",
... ]
```


### Common Gotchas

{{% notice info %}}
If you forget to include commas between your items, you'll get a `SyntaxError`.
{{% /notice %}}

```python
>>> numbers = [1, 2 3]
  File "<stdin>", line 1
    numbers = [1, 2 3]
                    ^
SyntaxError: invalid syntax
```

The REPL makes it difficult to forget the closing bracket, but if you forget it while writing code in a Python file, you'll see a `SyntaxError` with a different name. It'll say: `SyntaxError: unexpected EOF while parsing` or `SyntaxError: invalid syntax`.

For example:

```python
# Python file: program.py
names = ["Nina",
x = 5
```

Notice how the `SyntaxError` points to a completely valid line of Python code. In these cases, you also need to check the line of code **before** the line with the `SyntaxError`. There, we'll notice that we forgot the closing bracket of our `names` list.

```bash
# In a shell
(env) $ python program.py
  File "/Users/nina/Desktop/program.py", line 2
    x = 5
      ^
SyntaxError: invalid syntax
```

### Sorting

Sorting sounds complicated, but in practice, it's just one method call away!

#### Sorting a Copy Of Your List

If you'd like sort to return a brand new copy of your list, instead of modifying your original copy, you can use the built-in `sorted(my_list)` function on your list to return a *new* `list`, sorted in increasing (ascending) order. Or use `sorted(my_list, reverse=True)` to create a new `list` sorted backwards, in decreasing (or descending) order. This operation will **not modify** the underlying list.

Either of these operations will return a *new* list.

```python
>>> lottery_numbers = [1, 4, 32423, 2, 45, 11]
>>> sorted(lottery_numbers)
[1, 2, 4, 11, 45, 32423]
>>> lottery_numbers
[1, 4, 32423, 2, 45, 11]
>>> sorted(lottery_numbers, reverse=True)
[32423, 45, 11, 4, 2, 1]
>>> lottery_numbers
[1, 4, 32423, 2, 45, 11]
```

#### Sorting the list in-place

You can call `my_list.sort()` on your list to sort it in increasing (ascending) order, or `my_list.sort(reverse=True)` on the list to sort it backwards, in decreasing (or descending) order. This operation will modify the underlying list, and *doesn't return a value*.

```python
>>> lottery_numbers = [1, 4, 32423, 2, 45, 11]
>>> lottery_numbers.sort()
>>> lottery_numbers
[1, 2, 4, 11, 45, 32423]

>>> lottery_numbers.sort(reverse=True)
>>> lottery_numbers
[32423, 45, 11, 4, 2, 1]

>>> words = ["Umbrella", "Fox", "Apple"]
>>> words.sort()
>>> words
['Apple', 'Fox', 'Umbrella']
```

#### Reverse the list in-place

To reverse the items of a list in-place, call `my_list.reverse()` on it.

```python
>>> lottery_numbers = [1, 4, 32423, 2, 45, 11]
>>> lottery_numbers.reverse()
>>> lottery_numbers
[11, 45, 2, 32423, 4, 1]
```

### Finding Methods

Remember, if you ever forget which methods are available on `list`, just call `dir` on it. Ignore the methods that start with underscores. If you need help remembering what a method does, you can call `help()` on it. For example, for append, call `help(list.append)`.