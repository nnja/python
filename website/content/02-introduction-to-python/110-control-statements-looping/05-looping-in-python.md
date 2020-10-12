---
title: "Looping in Python"
date: 2019-02-10T18:21:55-08:00
draft: false
weight: 5
---

### `for` Loop Cheat Sheet

Looping in Python doesn't look like looping in other languages.

If you write JavaScript, Java, or other languages, you might have seen code that looks something like this code, that keeps track of 3 things: the starting index, the condition the loop will run until, and which action to take (in this case, incrementing the variable `i` by 1) until the condition is met.

```javascript
for (i = 0; i < 5; i++) {
  text += "The number is " + i + "<br>";
}
```

In fact, before these languages introduced something called a `for each` loop, that was also the clunky way you'd loop through items in a sequence.

### Looping in Python

Looping in Python is a simpler, cleaner process because the Python language prides itself on readability.

Remember you used the `in` keyword to test if an item was in a sequence? When combined with the `for` keyword, `in` can be used to indicate looping over each item in the sequence. The syntax is: `for single_item in items`, followed by a colon `:`, followed by a new line, a level of indentation, and the code you'd like to consider as the *body* of the loop. That is, the code that'll run multiple times, until there are no more items in the collection.

Let's see it in action.

```python
>>> colors = ["Red", "Green", "Blue", "Orange"]
>>> for color in colors:
...     print(f"The color is: {color}")
The color is: Red
The color is: Green
The color is: Blue
The color is: Orange
```

#### Looping over a range of numbers

Let's say we wanted to duplicate the code in the example JavaScript above, that prints out the numbers from 0 to 4.

In order to do this, we'll need to use a built-in function called `range()`. The range function in python produces a sequence of integers from an optional and inclusive start, to a defined and exclusive finish.


In Python2, this function created a list of each number in that sequence. As you can imagine, it was horribly inefficient for large ranges. In Python3, the `range()` function returns a new optimized data type. It's great for optimization, but it's harder for debugging.

{{% notice note %}}
If you want to explicitly see what a call to `range()` produces for debugging purposes, you can pass the result into the `list()` method to see all the values at once. For example: `list(range(5))`. Remember that this is inefficient, so use it for testing, not in production code.
{{% /notice %}}

If we wanted to loop over all the values from 0 to 4, we'd use the range function like this:

```python
>>> for num in range(5):
...     print(f"The number is: {num}")
...
The number is: 0
The number is: 1
The number is: 2
The number is: 3
The number is: 4
```

You'll notice that this call didn't *include* the number 5.

What if we wanted the range from 1 to 4, instead of 0 to 4? `range()` can be called with `start` and `stop` parameters, and the range will *start* from `start`.

```python
>>> for num in range(1, 5):
...     print(f"The number is: {num}")
...
The number is: 1
The number is: 2
The number is: 3
The number is: 4
```

You can also pass an a third optional `step` parameter in. Let's say I quickly wanted to print out all the even numbers from 2 to 10. I would call `range(2, 11, 2)`. Remember, 2 is where we're starting, 11 is one higher than where we're ending (10), and 2 is the step, or the amount to jump between numbers.

```python
>>> for num in range(2, 11, 2):
...     print(f"The number is: {num}")
...
The number is: 2
The number is: 4
The number is: 6
The number is: 8
The number is: 10
```

What do inclusive and exclusive mean in this context? *Exclusive* means that the end result *will not* include that number. If you'd like the numbers from 0 to 4, you would call `range(5)`. Consider 5 to the *stopping point*. *Inclusive* means the range will include the number. The `start` parameter is inclusive, meaning if you'd like the range of numbers from 1 to 4, you'd call `range(1, 5)`.

{{% notice tip %}}
If you can't remember how to use range, don't forget to call `help(range)` from the command line.
{{% /notice %}}

#### Looping over items with the index using `enumerate`.

In Python, we avoid writing code like the JavaScript `for` loop at the top, but sometimes it's unavoidable, and we need a way to access the index of the items we're looping through. To do that we use a special function called `enumerate()`. The function takes a sequence, like a `list`, and it *returns* a `list` of tuples, containing the index of the item in the sequence, and the sequence itself.

Don't worry about the list of tuples for now, but remember our tuple unpacking from earlier?

```python
>>> point = (2, 5, 11)
>>> x, y, z = point
>>> x
2
>>> y
5
>>> z
11
```

Because `enumerate()` returns a structure that looks like a list of `tuple`s under the hood, we can take advantage of tuple unpacking in the `for` loop.

```python
>>> for index, item in enumerate(colors):
...     print(f"Item: {item} is at index: {index}.")
...
Item: Red is at index: 0.
Item: Green is at index: 1.
Item: Blue is at index: 2.
Item: Orange is at index: 3.
```

{{% notice tip %}}
Remember, indicies in Python start at zero.
{{% /notice %}}

#### Looping over a dictionary

Now that we know we can use tuple unpacking in a for loop, let's go over how to loop over a dictionary.

Let's say we have a dictionary of colors to their hex color code used for HTML in websites.

```python
>>> hex_colors = {
...     "Red": "#FF",
...     "Green": "#008",
...     "Blue": "#0000FF",
... }
```

{{% notice warning %}}
Remember, a dictionary is composed of key, value pairs. When we loop over a dictionary with the `for item in my_dict` syntax, we'll end up looping over **just** the keys.
{{% /notice %}}

In this example, notice how we're looping over the wrong thing:

```python
>>> for color in hex_colors:
...     print(f"The value of color is actually: {color}")
...
The value of color is actually: Red
The value of color is actually: Green
The value of color is actually: Blue
```

{{% notice tip %}}
If we want to loop over the key, value pairs in a dictionary, we'll want to call `my_dict.items()`.
{{% /notice %}}

We can use tuple unpacking along with the `my_dict.items()` list to loop over both the keys and the values at the same time.

```python
>>> for color, hex_value in hex_colors.items():
...     print(f"For color {color}, the hex value is: {hex_value}")
...
For color Red, the hex value is: #FF0000
For color Green, the hex value is: #008000
For color Blue, the hex value is: #0000FF
```

##### Common Errors

What if you try to loop over key, value pairs, and forget to use `my_dict.items()`?

```python
>>> for color, hex_value in hex_colors:
...     print(f"For color {color}, the hex value is: {hex_value}")
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
```

{{% notice info %}}
You'll see `ValueError: too many values to unpack (expected 2)` if you *forget* to call `my_dict.items()`, and try to loop over what you'd expect to be key, value pairs.
{{% /notice %}}

#### Additional Resources

If you really want to be a pro at looping in a Pythonic way, I recommend watching Raymond Hettinger's talk - [Transforming Code into Beautiful, Idiomatic Python](https://www.youtube.com/watch?time_continue=1855&v=OSGv2VnC0go) after the course.