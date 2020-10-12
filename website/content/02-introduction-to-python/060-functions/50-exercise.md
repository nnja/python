---
title: "Practice"
date: 2019-03-02T00:00:00-08:00
draft: false
weight: 50
pre: "<b>⭐️ </b>"
---

## Functions

Let's try creating a basic function. Use tab to indent the second line, and press enter on an empty line to finish the function.

```python
>>> def add_numbers(x, y):
...     return x + y
... # Press Enter
```

Now let's try our new function. Type this into your REPL:

```python
>>> add_numbers(1, 2)
# Let's use the string formatting we learned in the last chapter
>>> print(f"The sum of 1 and 2 is {add_numbers(1, 2)}")
```

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> add_numbers(1, 2)
3
# Let's use the string formatting we learned in the last chapter
>>> print(f"The sum of 1 and 2 is {add_numbers(1, 2)}")
The sum of 1 and 2 is 3
```

{{% /expand%}}


## The Importance of Whitespace

Here's an error that you'll become very familiar with during your career as a Pythonista, the `IndentationError`. Whitespace is important for defining function scope in python, so missing or extra indentations or spaces will cause the runtime to throw this error. Let's redefine our `add_numbers` function, but we'll forget to indent the second line, `return x + y`. Notice that the second line is directly under (at the same indentation level) as the `def`:

```python
>>> def add_numbers(x, y):
... return x + y
  File "<stdin>", line 2
    return x + y
         ^
IndentationError: expected an indented block
```

Notice how the runtime tells us the line that failed (`line 2`), gives you a copy of the line with an arrow pointing to the offending error (`return x + y`), and then tells you the error (`IndentationError`) with additional information (`expected an indented block`).

## Function Scope

As we saw earlier, scoping in Python happens with whitespace. Let's see this in action:

```python
>>> x = 1
>>> y = 2
>>> def add_numbers(x, y):
...     print(f"Inside the function, x = {x} and y = {y}")
...     return x + y
...
>>> print(f"Outside the function, x = {x} and y = {y}")
>>> print(f"The sum of 5 and 6 is {add_numbers(5, 6)}")
```

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> x = 1
>>> y = 2
>>> def add_numbers(x, y):
...     print(f"Inside the function, x = {x} and y = {y}")
...     return x + y
...
>>> print(f"Outside the function, x = {x} and y = {y}")
Outside the function, x = 1 and y = 2
>>>
>>> print(f"The sum of 5 and 6 is {add_numbers(5, 6)}")
Inside the function, x = 5 and y = 6
The sum of 5 and 6 is 11
```

{{% /expand%}}


## Positional Arguments vs Keyword Arguments

The `x` and `y` arguments for our `add_numbers()` function are called positional arguments. Python also lets us declare *keyword* arguments. Keyword arguments are great for setting default values, because passing them is optional. Just remember that keyword arguments must come *after* any positional arguments. Let's make a more generic function for doing math:

```python
>>> def calculate_numbers(x, y, operation="add"):
...     if operation == "add":
...         return x + y
...     elif operation == "subtract":
...         return x - y
...
# Let's try our new function. Remember, if we don't pass the operation keyword argument, the default is "add"
>>> calculate_numbers(2, 3)
# You can pass a keyword argument as a normal positional argument
>>> calculate_numbers(2, 3, "subtract")
# You can also use the argument's keyword. This helps with readability
>>> calculate_numbers(2, 3, operation="subtract")
```

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> def calculate_numbers(x, y, operation="add"):
...     if operation == "add":
...         return x + y
...     elif operation == "subtract":
...         return x - y
...
# Let's try our new function. Remember, if we don't pass the operation keyword argument, the default is "add"
>>> calculate_numbers(2, 3)
5
# You can pass a keyword argument as a normal positional argument
>>> calculate_numbers(2, 3, "subtract")
-1
# You can also use the argument's keyword. This helps with readability
>>> calculate_numbers(2, 3, operation="subtract")
-1
```

{{% /expand%}}
