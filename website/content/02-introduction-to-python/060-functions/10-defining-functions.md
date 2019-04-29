---
title: "Defining Functions"
date: 2019-02-10T18:16:01-08:00
draft: false
weight: 10
---

The purpose of functions in Python are to create reusable code. If we find ourselves copying and pasting the same code multiple times, that's a good sign that a function might help!

### Anatomy of a function

This is the recipe for defining a Python function:

1. `def`: the `def` keyword, telling Python we're about to start a function definition
1. a name for the function
1. `(`: opening parenthesis
1. (optional) the **names** of one or more arguments, separated with `,`
1. (optional) the **names** and **values** of one or more default arguments, separated with (`,`) *note: we'll see these in the next section*
1. `)` closing parenthesis
1. `:` a colon

A function in Python is defined with the `def` keyword, followed by the function names, zero or more argument names contained in parenthesis `()`, and a colon `:` to indicate the start of the function.

The contents of the function then follow.

Then, an *optional* `return` statement can follow, if the function plans on passing data back to the caller.

```python
# A Basic Function that accepts no arguments and returns nothing.
def hello_world():
    print("Hello, World!")


# A Function that accepts two arguments, and returns the value of
# those numbers added together.
def add_numbers(x, y):
    return x + y
```

{{% notice tip %}}
If you **forget** the recipe while trying to create a function, Python will help you remember with a `SyntaxError`.
{{% /notice %}}

For example, trying to create a function without the colon `:`:

```python
>>> def hello_world()
  File "<stdin>", line 1
    def hello_world()
                    ^
SyntaxError: invalid syntax
```

And trying to create a function without the parenthesis `()`:

```python
>>> def hello_world:
  File "<stdin>", line 1
    def hello_world:
                   ^
SyntaxError: invalid syntax
```

### Function Contents

The recipe for function contents:

1. a new line
1. indentation (press tab on your keyboard)
1. one or more lines
1. (optional) a `return` statement

#### `return` statement

A `return` statement is a way to "short-circuit" the function.

Using a `return` statement, you can optionally pass back data to the caller of your function.

##### with no `return` statement

If a function doesn't have a return statement, it implicitly returns `None`.

```python
>>> def foo():
...     x = 5
...
>>> val = foo()
>>> type(val)
<type 'NoneType'>
```

##### with a `return` statement, but no value

If a function has a return statement, but no value, it also returns `None`. This is typically used to control the flow of a program.

```python
>>> def foo():
...     x = 5
...     return
...
>>> val = foo()
>>> type(val)
<type 'NoneType'>
```

##### with a `return` statement and a value

To return a value from a function, just type it after the `return` statement. You can return anything from a Python function, including other functions! For today, we'll focus on simple and complex data types.

```python
>>> def foo():
...     x = 5
...     return x
...
>>> val = foo()
>>> val
5
```

As we explore simple functions, our `return` statements will usually be at the end of the function, but that's not the only way they can be used. A function can have multiple `return` statements, and those `return` statements can be used to help control the flow of the program.

{{% notice note %}}
Note: Because it's syntactically correct to have multiple return statements in a function, it's up to you to use them correctly. If you use a linter for your code files and you place additional code in a function **after** a return statement, the
linter will give you a helpful hint about the rest of the code being unreachable.
{{% /notice %}}

#### Indentation

One of the most important aspects of functions is indentation. Remember, Python doesn't use curly braces to figure out what's inside a function like other languages you've seen like JavaScript or Java.

Python knows what code is related to a function by how it's indented. Anything that's indented one level deep under the function declaration is part of the function, no matter how many spaces there are between lines.

To add a level of indentation, just press the **Tab** key on your keyboard after entering a new line.

If you're using the REPL, once you're done entering your function, you'll need to press enter an additional time, to mark the end of the function. You know you're done defining your function when you see the 3 input arrows `>>>` again.

Let's try it together. Type the following code in your REPL. Note that the 3 dots '...' indicate that those lines are *indented* in the REPL. If you type your code in a Python file, you won't see the `...` dots.

```python
>>> def add_numbers(x, y):
...     return x + y
...
```

{{%expand "See an error? Expand this section." %}}
Note: If you get an `IndentationError`, that means that you didn't correctly indent your code after your function definition. Try typing your function into the REPL one more time.

```python
# The error you'll see if you didn't indent your function correctly.
>>> def add_numbers(x, y):
... return x + y
File "<stdin>", line 2
    return x + y
        ^
IndentationError: expected an indented block
```
{{% /expand%}}

### Calling Functions

#### With no arguments

Once you've defined a function, you can call it from your Python code as many times as you'd like.

To call a Python function, type in it's name, along with parenthesis, and any *required* arguments to the function. Let's try it now, with a function that doesn't require arguments.

```python
>>> def hello_world():
...     print("Hello, World!")
...
>>> hello_world()
Hello, World!
```

#### With arguments

Let's try it again, this time with a function that does accept arguments.

{{% notice tip %}}
Here, note that the function accepts **names** for the arguments. But, when we call the function, we're passing in **values**.
{{% /notice %}}

```python
>>> def add_numbers(x, y):
...     return x + y
...
>>> add_numbers(3, 5)
8
>>>
```

#### Storing the `return`ed value of a function.

Storing the `return`ed value of a function is easy. All you need to do is assign it to a variable.

Let's try it now.

```python
>>> def add_numbers(x, y):
...     return x + y
...
>>> new_number = add_numbers(3, 5)
>>> new_number
8
```

The variable `new_number` now contains the result of running our `add_numbers` function with our arguments `3` and `5`.
