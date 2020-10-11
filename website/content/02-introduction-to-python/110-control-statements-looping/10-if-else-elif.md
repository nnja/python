---
title: "if, else, elif"
date: 2019-02-10T18:20:07-08:00
draft: false
weight: 10
---

### The `if` Statement and Conditionals

`if` in Python means: **only run the rest of this code once, *if* the condition evaluates to `True`.** Don't run the rest of the code at all if it's not.

Anatomy of an `if` statement: Start with the `if` keyword, followed by a boolean value, an expression that evaluates to `True`, or a value with "Truthiness". Add a colon `:`, a new line, and write the code that will run if the statement is `True` under a level of indentation.

{{% notice note %}}
Remember, just like with functions, we know that code is associated with an `if` statement *by it's level of indentation*. All the lines indented under the `if` statement will run if it evaluates to `True`.
{{% /notice %}}

```python
>>> if 3 < 5:
...     print("Hello, World!")
...
Hello, World!
```

{{% notice tip %}}
Remember, your `if` statements only run if the expression in them evaluates to `True` and just like with functions, you'll need to enter an extra space in the REPL to run it.
{{% /notice %}}

#### Using `not` With `if` Statements

If you only want your code to run if the expression is `False`, use the `not` keyword.

```python
>>> b = False
>>> if not b:
...     print("Negation in action!")
...
Negation in action!
```

### `if` Statements and Truthiness

`if` statements also work with items that have a "truthiness" to them.

For example:

 * The number 0 is False-y, any other number (including negatives) is Truth-y
 * An empty `list`, `set`, `tuple` or `dict` is False-y
 * Any of those structures with items in it is Truth-y

```python
>>> message = "Hi there."

>>> a = 0
>>> if a:   # 0 is False-y
...     print(message)
...

>>> b = -1
>>> if b:  # -1 is Truth-y
...     print(message)
...
Hi there.

>>> c = []
>>> if c:  # Empty list is False-y
...     print(message)
...

>>> d = [1, 2, 3]
>>> if d:  # List with items is Truth-y
...     print(message)
...
Hi there.
```

### `if` Statements and Functions

You can easily declare `if` statements in your functions, you just need to mindful of the level of indentation. Notice how the code belonging to the `if` statement is indented at *two levels*.

```python
>>> def modify_name(name):
...    if len(name) < 5:
...         return name.upper()
...    else:
...         return name.lower()
...
>>> name = "Nina"
>>> modify_name(name)
'NINA'
```

#### Nested `if` Statements

Using the same technique, you can also *nest* your `if` statements.

```python
>>> def num_info(num):
...    if num > 0:
...        print("Greater than zero")
...        if num > 10:
...            print("Also greater than 10.")
...
>>> num_info(1)
Greater than zero
>>> num_info(15)
Greater than zero
Also greater than 10.
```


#### How *Not* To Use `if` Statements

Remember, comparisons in Python evaluate to `True` or `False`. With conditional statements, we check for that value *implicitly*. In Python, we **do not** want to compare to `True` or `False` with `==`.

{{% notice warning %}}
Warning - pay attention, because the code below shows what you **shouldn't** do.
{{% /notice %}}

```python
# Warning: Don't do this!
>>> if (3 < 5) == True: # Warning: Don't do this!
...     print("Hello")
...
Hello

# Warning: Don't do this!
>>> if (3 < 5) is True: # Warning: Don't do this!
...     print("Hello")
...
Hello
```

{{% notice tip %}}
Do this instead:
{{% /notice %}}

```python
>>> if 3 < 5:
...     print("Hello")
...
Hello
```

If we want to explicitly check if the value is explicitly set to `True` or `False`, we can use the `is` keyword.

```python
>>> a = True        # a is set to True
>>> b = [1, 2, 3]   # b is a list with items, is "truthy"
>>>
>>> if a and b:     # this is True, a is True, b is "truthy"
...     print("Hello")
...
Hello
>>> if a is True:   # we can explicitly check if a is True
...     print("Hello")
...
Hello
>>> if b is True:   # b does not contain the actual value of True.
...     print("Hello")
...
>>>
```

### `else`

The `else` statement is what you want to run **if and only if** your `if` statement wasn't triggered.

An `else` statement is part of an `if` statement. If your `if` statement ran, your `else` statement will never run.


```python
>>> a = True
>>> if a:
...     print("Hello")
... else:
...     print("Goodbye")
...
Hello
```

And vice-versa.

```python
>>> a = False
>>> if a:
...     print("Hello")
... else:
...     print("Goodbye")
...
Goodbye
```

In the REPL it must be written on the line after your last line of indented code. In Python code in a file, there can't be any other code between the `if` and the `else`.

{{% notice info %}}
You'll see `SyntaxError: invalid syntax` if you try to write an `else` statement on its own, or put extra code between the `if` and the `else` in a Python file.
{{% /notice %}}

```python
>>> if a:
...     print("Hello")
...
Hello
>>> else:
  File "<stdin>", line 1
    else:
       ^
SyntaxError: invalid syntax
```

### `elif` Means Else, If.

`elif` means *else if*. It means, **if** this `if` statement isn't considered `True`, try this **instead.**

You can have as many `elif` statements in your code as you want. They get evaluated in the order that they're declared **until** Python finds one that's `True`. That runs the code defined in that `elif`, and skips the rest.

```python
>>> a = 5
>>> if a > 10:
...     print("Greater than 10")
... elif a < 10:
...     print("Less than 10")
... elif a < 20:
...     print("Less than 20")
... else:
...     print("Dunno")
...
Less than 10
```