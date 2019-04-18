---
title: "Practice"
date: 2019-03-08T00:00:00-08:00
draft: false
weight: 50
pre: "<b>⭐️ </b>"
---

## Control statements and looping

### `if`, `else`, and `elif`

Let's practice our branching statements. Remember that `elif` (short for `else if`) is an optional branch that will let you add another `if` test, and `else` is an optional branch that will catch anything not previously caught by `if` or `elif`.

```python
>>> def test_number(number):
...     if number < 100:
...         print("This is a pretty small number")
...     elif number == 100:
...         print("This number is alright")
...     else:
...         print("This number is huge!")
...
>>> test_number(5)
>>> test_number(99)
>>> test_number(100)
>>> test_number(8675309)
```

{{%expand "Here's what you should have seen in your REPL:" %}}
```python
>>> def test_number(number):
...     if number < 100:
...         print("This is a pretty small number")
...     elif number == 100:
...         print("This number is alright")
...     else:
...         print("This number is huge!")
...
>>> test_number(5)
This is a pretty small number
>>> test_number(99)
This is a pretty small number
>>> test_number(100)
This number is alright
>>> test_number(8675309)
This number is huge!
```
{{%/expand%}}

You can also have multiple conditions in an if statement. This function prints "Fizzbuzz!" if the number is divisible by both 3 and 5 (the `%` or modulo operator returns the remainder from the division of two numbers):

```python
>>> def fizzbuzz(number):
...     if number % 3 == 0 and number % 5 == 0:
...         print("Fizzbuzz!")
...
>>> fizzbuzz(3)
>>> fizzbuzz(5)
>>> fizzbuzz(15)
```

{{%expand "Here's what you should have seen in your REPL:" %}}
```python
>>> def fizzbuzz(number):
...     if number % 3 == 0 and number % 5 == 0:
...         print("Fizzbuzz!")
...
>>> fizzbuzz(3)
>>> fizzbuzz(5)
>>> fizzbuzz(15)
Fizzbuzz!
```
{{%/expand%}}

Let's also practice using `if` to test for an empty list. Remember that an empty list is "Falsey", or resolves to `False`. Write a function to print a list of elements, or an error message if the list is empty. Print a special message if a list item is `None`:

```python
>>> def my_func(my_list):
...     if my_list:
...         for item in my_list:
...             if item is None:
...                 print("Got None!")
...             else:
...                 print(item)
...     else:
...         print("Got an empty list!")
...
>>> my_func([1, 2, 3])
1
2
3
>>> my_func([2, None, "hello", 42])
2
Got None!
hello
42
>>> my_func([])
Got an empty list!
```


## The `for` loop, `range()` and `enumerate()`

Let's try making a list and looping over it:

```python
>>> my_list = [0, 1, 2]
>>> for num in my_list:
...     print(f"Next value: {num}")
...
```


If we're just interested in looping over a list of numbers, we can use the `range()` function instead. Remember that the first argument is inclusive and the second is exclusive:

```python
>>> for num in range(0, 3):
...     print(f"Next value: {num}")
...
```

Another useful function is `enumerate()`, which iterates over an iterable (like a list) and also gives you an automatic counter. `enumerate()` returns a tuple in the form of (`counter`, `item`).

```python
>>> my_list = ["foo", "bar", "baz"]
>>> for index, item in enumerate(my_list):
...     print(f"Item {index}: {item}")
...
```

We can also loop over a dictionary's keys and/or values. If you try to iterate over the dictionary object itself, what do you get?

```python
>>> my_dict = {"foo": "bar", "hello": "world"}
>>> for key in my_dict:
...     print(f"Key: {key}")
...
# This is equivalent to...
>>> for key in my_dict.keys():
...     print(f"Key: {key}")
...
```

The `keys()` method returns the dictionary's keys as a list, which you can then iterate over as you would any other list. This also works for `values()`

```python
>>> for value in my_dict.values():
...     print(f"Value: {value}")
...
```

The most useful function, however, is `items()`, which returns the dictionary's items as tuples in the form of (key, value):

```python
>>> for key, value in my_dict.items():
...     print(f"Item {key} = {value}")
...
```

{{%expand "Here's what you should have seen in your REPL:" %}}
```python
>>> my_list = [1, 2, 3]
>>> for num in my_list:
...     print(f"Next value: {num}")
...
Next value: 0
Next value: 1
Next value: 2
```

```python
>>> for num in range(0, 3):
...     print(f"Next value: {num}")
...
Next value: 0
Next value: 1
Next value: 2
```

```python
>>> my_list = ["foo", "bar", "baz"]
>>> for index, item in enumerate(my_list):
...     print(f"Item {index}: {item}")
...
Item 0: foo
Item 1: bar
Item 2: baz
```

```python
>>> my_dict = {"foo": "bar", "hello": "world"}
>>> for key in my_dict:
...     print(f"Key: {key}")
...
Key: foo
Key: hello

>>> for key in my_dict.keys():
...     print(f"Key: {key}")
...
Key: foo
Key: hello

>>> for value in my_dict.values():
...     print(f"Value: {value}")
...
Value: bar
Value: world

>>> for key, value in my_dict.items():
...     print(f"Item {key} = {value}")
...
Item foo = bar
Item hello = world
```

{{%/expand%}}

## `break`, `continue`, and `return`

`break` and `continue` are important functions for controlling the program flow inside loops. `break` ends the loop immediately and continues executing from outside the loop's scope, and `continue` skips the remainder of the loop and continues executing from the next round of the loop. Let's practice:

```python
>>> for num in range(0, 100):
...     print(f"Testing number {num}")
...     if num == 3:
...         print("Found number 3!")
...         break
...     print("Not yet...")
...
```

Notice that "Not yet..." doesn't get printed for number 3, because we `break` out of the loop first. Let's try a `continue`:

```python
>>> for num in range(0, 100):
...     print(f"Testing number {num}")
...     if num < 3:
...         continue
...     elif num == 5:
...         print("Found number 5!")
...         break
...     print("Not yet...")
...
```

Notice that "Not yet..." doesn't get printed at all until the number is 3, because the `continue` short-circuits the loop back to the beginning. Then we `break` when we hit 5.

You can also use the `return` keyword to break out of a loop within a function, while optionally returning a value.

```python
>>> def is_number_in_list(number_to_check, list_to_search):
...     for num in list_to_search:
...         print(f"Checking {num}...")
...         if num == number_to_check:
...             return True
...     return False
>>> my_list = [1, 2, 3, 4, 5]
>>> is_number_in_list(27, my_list)
>>> is_number_in_list(2, my_list)
```

Notice that our function `is_number_in_list` checks all the numbers in `my_list` on the first run, but on the next run, stops immediately when it hits 3 and returns `True`.

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> for num in range(0, 100):
...     print(f"Testing number {num}")
...     if num == 3:
...         print("Found number 3!")
...         break
...     print("Not yet...")
...
Testing number 0
Not yet...
Testing number 1
Not yet...
Testing number 2
Not yet...
Testing number 3
Found number 3!
>>>
```

```python
>>> for num in range(0, 100):
...     print(f"Testing number {num}")
...     if num < 3:
...         continue
...     elif num == 5:
...         print("Found number 5!")
...         break
...     print("Not yet...")
...
Testing number 0
Testing number 1
Testing number 2
Testing number 3
Not yet...
Testing number 4
Not yet...
Testing number 5
Found number 5!
```

```python
>>> def is_number_in_list(number_to_check, list_to_search):
...     for num in list_to_search:
...         print(f"Checking {num}...")
...         if num == number_to_check:
...             return True
...     return False
...
>>> is_number_in_list(27, my_list)
Checking 1...
Checking 2...
Checking 3...
Checking 4...
Checking 5...
False
>>> is_number_in_list(2, my_list)
Checking 1...
Checking 2...
True
```
{{%/expand%}}

## `while` loop

Instead of looping over a sequence, `while` loops continue looping while a certain condition is met (or not met). The condition is checked at the beginning every iteration.

```python
>>> counter = 0
>>> while counter < 3:
...     print(f"Counter = {counter}")
...     counter += 1
```

Notice that the loop ends once `counter` 3, and the remainder of the loop is bypassed. You can also loop forever by using `while True` or `while False`, but you should make sure you have solid `break` conditions, or your program will just loop forever (unless that's what you want).

```python
>>> counter = 0
>>> while True:
...     print(f"Counter = {counter}")
...     if counter == 3:
...         break
...     counter += 1
```

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> counter = 0
>>> while counter < 3:
...     print(f"Counter = {counter}")
...     counter += 1
...
Counter = 0
Counter = 1
Counter = 2
```

```python
>>> counter = 0
>>> while True:
...     print(f"Counter = {counter}")
...     if counter == 3:
...         break
...     counter += 1
...
Counter = 0
Counter = 1
Counter = 2
Counter = 3
```

{{%/expand%}}

## Nested Loops

Nesting loops is often necessary and sometimes tricky. The `break` keyword will only get you out of whichever loop you're `break`ing. The only way to exit all loops is with multiple `break` statements (at each level), or the `return` keyword (inside a function). For example:

```python
names = ["Rose", "Max", "Nina"]
target_letter = 'x'
found = False

for name in names:
    for char in name:
            if char == target_letter:
                    found = True
                    break

    if found:
        print(f"Found {name} with letter: {target_letter}")
        break
```

Or:

```python
>>> for x in range(0, 5):
...     for y in range(0, 5):
...         print(f"x = {x}, y = {y}")
...         if y == 2:
...             break
...
```

Notice how the inner `y` loop never gets above 2, whereas the outer `x` loop continues until the end of its range.

{{%expand "Here's what you should have seen in your REPL:" %}}
```python
>>> for x in range(0, 5):
...     for y in range(0, 5):
...         print(f"x = {x}, y = {y}")
...         if y == 2:
...             break
...
x = 0, y = 0
x = 0, y = 1
x = 0, y = 2
x = 1, y = 0
x = 1, y = 1
x = 1, y = 2
x = 2, y = 0
x = 2, y = 1
x = 2, y = 2
x = 3, y = 0
x = 3, y = 1
x = 3, y = 2
x = 4, y = 0
x = 4, y = 1
x = 4, y = 2
```
{{%/expand%}}