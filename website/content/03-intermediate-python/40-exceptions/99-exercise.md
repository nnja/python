---
title: "Practice"
date: 2019-03-09T00:00:00-08:00
draft: false
weight: 10
pre: "<b>⭐️ </b>"
---

### Syntax Errors

Let's get more comfortable with exceptions. First, you've probably seen this one already: The `IndentationError`.

```python
>>> def my_function():
... print("Hello!")
  File "<stdin>", line 2
    print("Hello!")
        ^
IndentationError: expected an indented block
```

Notice that we started a new function scope with the `def` keyword, but didn't indent the next line of the function, the `print()` argument.

You've probably also seen the more general `SyntaxError`. This one's probably obvious - something is misspelled, or the syntax is otherwise wrong. Python gives us a helpful little caret `^` under the earliest point where the error was detected, however you'll have to learn to read this with a critical eye as sometimes the actual mistake precedes the invalid syntax. For example:

```python
>>> a = [4,
... x = 5
  File "<stdin>", line 2
    x = 5
      ^
SyntaxError: invalid syntax
```

Here, the invalid syntax is `x = 5`, because assignment statements aren't valid list elements, however the actual error is the missing right bracket `]` on the line above.

### Common Exceptions

You'll get plenty of practice triggering syntax errors on your own. Let's practice triggering some exceptions. Type this *perfectly valid* code into your REPL and see what happens:

```python
>>> a = 1 / 0
```

{{%expand "Here's what you should have seen in your REPL:" %}}
```python
>>> a = 1 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```
{{% /expand%}}

Of course, you'll get a divide-by-zero error, or as Python calls it, `ZeroDivisionError`. Some other common errors are `TypeError` when trying to perform an action on two unrelated types, `KeyError` when trying to access a dictionary key that doesn't exist, and `AttributeError` when trying to access a variable or call a function that doesn't exist on an object.

```python
>>> 2 + "3"

>>> my_dict = {"hello": "world"}
>>> my_dict["foo"]

>>> my_dict.append("foo")
```

{{%expand "Here's what you should have seen in your REPL:" %}}
```python
>>> 2 + "3"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'

>>> my_dict = {"hello": "world"}
>>> my_dict["foo"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'foo'

>>> my_dict.append("foo")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'append'
```
{{% /expand%}}


### Raising our own Exceptions

Making our own Exceptions is cheap and easy, and useful for keeping track of various error states that are specific to your application. Simply inherit from the general `Exception` class:

```python
>>> class MyException(Exception):
...     pass
>>> raise MyException()
```

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> class MyException(Exception):
...     pass
>>> raise MyException()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyException
```
{{% /expand%}}

It's also sometimes helpful to change the default behavior for your custom Exceptions. In this case, you can simply provide your own `__init__()` method inside your Exception subclass:


```python
class MyException(Exception):
...     def __init__(self, message):
...         new_message = f"!!!ERROR!!! {message}"
...         super().__init__(new_message)
...
>>> raise MyException("Something went wrong!")
```
{{%expand "Here's what you should have seen in your REPL:" %}}

```python
class MyException(Exception):
...     def __init__(self, message):
...         new_message = f"!!!ERROR!!! {message}"
...         super().__init__(new_message)
...
>>> raise MyException("Something went wrong!")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyException: !!!ERROR!!! Something went wrong!
```
{{% /expand%}}

### `try`, `except`

In Python, the "try-catch" statements use `try` and `except`. As we discussed, `try` is the code that could possibly throw an Exception, and `except` is the code that runs if the error is raised. Practice catching a `KeyError` by `try`ing to access a fake dictionary key:

```python
>>> try:
...     my_dict = {"hello": "world"}
...     print(my_dict["foo"])
... except KeyError:
...     print("Oh no! That key doesn't exist")
...
```

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> try:
...     my_dict = {"hello": "world"}
...     print(my_dict["foo"])
... except KeyError:
...     print("Oh no! That key doesn't exist")
...
Oh no! That key doesn't exist
```
{{% /expand%}}

Let's add in catching the specific `KeyError` object so that we can access it during the `except` block:

```python
>>> try:
...     my_dict = {"hello": "world"}
...     print(my_dict["foo"])
... except KeyError as key_error:
...     print(f"Oh no! The key {key_error} doesn't exist!")
...
```

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> try:
...     my_dict = {"hello": "world"}
...     print(my_dict["foo"])
... except KeyError as key_error:
...     print(f"Oh no! The key {key_error} doesn't exist!")
...
Oh no! The key 'foo' doesn't exist!
```
{{% /expand%}}


### Re-Raising

Sometimes it's helpful to catch an error, perform an action, and then pass the error on rather than swallowing it. This is useful when, for example, something goes wrong deep inside your code and you need to perform a special action, but also let code further up the chain know that something is wrong and the program can't continue. Let's divide one number by other, decrementing until we hit zero. Catch that error and immediately raise a `RuntimeError`:

```python
>>> while True:
...     for divisor in range(5, -1, -1):
...         try:
...             quotient = 10 / divisor
...             print(f"10 / {divisor} = {quotient}")
...         except ZeroDivisionError:
...             print("Oops! We tried to divide by zero!")
...             raise RuntimeError
...
```

{{%expand "Here's what you should have seen in your REPL:" %}}

```python
>>> while True:
...     for divisor in range(5, -1, -1):
...         try:
...             quotient = 10 / divisor
...             print(f"10 / {divisor} = {quotient}")
...         except ZeroDivisionError:
...             print("Oops! We tried to divide by zero!")
...             raise RuntimeError
...
10 / 5 = 2.0
10 / 4 = 2.5
10 / 3 = 3.3333333333333335
10 / 2 = 5.0
10 / 1 = 10.0
Oops! We tried to divide by zero!
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 8, in <module>
RuntimeError
```

What happened here? We got two exceptions! First, our code hit the `ZeroDivisionError`, which we caught, and printed our "Oops!" message. Then, the interpreter saw that we raised a `RuntimeError`, which we didn't catch, so it broke us out of our `while True` loop and ended the program with a Traceback.

{{% /expand%}}
