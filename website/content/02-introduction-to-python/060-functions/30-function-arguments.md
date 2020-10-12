---
title: "Function Arguments"
date: 2019-02-10T18:16:14-08:00
draft: false
weight: 30
---

### Arguments in Practice

### Positional arguments are required

Positional arguments are all required, and must be given in the order they are declared.

For example, this function doesn't do what we expected, because we passed in our arguments in the wrong order.

In the REPL:

```python
>>> def say_greeting(name, greeting):
...     print(f"{greeting}, {name}.")
...
>>> say_greeting("Hello!", "Nina")
Nina, Hello!.
```

### Keyword arguments with default values

Functions can accept two types of named arguments, ones without default values, and ones with default values. Arguments that have default values are called **keyword arguments**. The nice thing about defaults is they can be overridden when needed.

Let's see this in practice, by writing two functions that print out a greeting. One function will have a default argument to make things easier for us.

```python
# No default arguments
def say_greeting(greeting, name):
    print(f"{greeting}, {name}.")

# Default argument - greeting will always be
# Hello, if one isn't provided.
def say_greeting_with_default(name, greeting="Hello", punctuation="!"):
    print(f"{greeting}, {name}{punctuation}")
```

#### Without default arguments

Now, in the REPL, let's try calling our function with no default arguments:

```python
>>> # No Default arguments
>>> def say_greeting(greeting, name):
...     print(f"{greeting}, {name}.")
...
>>> say_greeting("Good Day", "Nina")
Good Day, Nina.
```

#### Using default arguments

Let's make a new function, `say_greeting_with_default` that accepts two arguments -- `name`, and a now **optional** argument, `greeting`. If `greeting` is not passed in, it will default to `Hello`.

In the REPL:

```python
>>> # With Default Arguments
>>> def say_greeting_with_default(name, greeting="Hello", punctuation="!"):
...     print(f"{greeting}, {name}{punctuation}")
...
>>> say_greeting_with_default("Nina")
Hello, Nina!
>>> say_greeting_with_default("Nina", "Good Day")
Good Day, Nina!
```

#### Order matters!

A function can accept all of one type or the other, but arguments need to go in a specific order.

All of the *required arguments go first*. They are then *followed by the optional keyword arguments*.

What happens when we try to define our arguments out of order? If you guessed a `SyntaxError`, you're correct!

```python
>>> def say_greeting_bad(greeting="Hello", name):
...     print("Oops, this won't work!")
...
  File "<stdin>", line 1
SyntaxError: non-default argument follows default argument
```

### Calling functions with arguments

There are a few important things to know about calling functions with arguments.

#### Arguments without defaults are **required**!

Arguments without default values are **required** by Python. Otherwise your function wouldn't know what to do! If you don't pass in all the required arguments, you'll get a `TypeError`.

In the REPL:
```python
>>> def say_greeting(name, greeting):
...     print(f"{greeting}, {name}.")
...
>>> say_greeting("Nina")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: say_greeting() missing 1 required positional argument: 'greeting'
```

#### You can pass in none, some, or all of the keyword arguments.

If your function takes keyword arguments, you can provide zero, one, or all of them when you call it. You don't need to pass these arguments in order either.

```python
>>> def create_query(language="JavaScipt", num_stars=50, sort="desc"):
...     return f"language:{language} num_stars:{num_stars} sort:{sort}"
...
>>> create_query()
'language:JavaScipt num_stars:50 sort:desc'
>>> create_query(language="Ruby")
'language:Ruby num_stars:50 sort:desc'
>>> create_query(num_stars=1, language="Python", sort="asc")
'language:Python num_stars:1 sort:asc'
```

#### You can pass in required parameters by keyword.

Even if your function arguments don't have keyword arguments with defaults, you can still pass values in to the function by name. This is especially helpful if you want to be extra clear about what you're passing in.

```python
>>> def say_greeting(name, greeting):
...     print(f"{greeting}, {name}.")
...
>>> say_greeting("Nina", "Hello")
Hello, Nina.
>>> say_greeting(name="Max", greeting="Bonjour")
Bonjour, Max.
```

### Arguments Danger Zone

{{% notice warning %}}
Never use mutable types, like `list`s as a default argument.
{{% /notice %}}

We'll talk more about `list`s and mutability in the coming chapter, but for the time being remember to never use an empty list as a default value to a function.

Why? Because it won't work like you'd expect it to.

```python
>>> # Don't do this!
>>> def add_five_to_list(my_list=[]):
...     my_list.append(5)
...     return my_list
...
>>> # This works like we expected it to.
>>> add_five_to_list()
[5]
>>> # Huh?
>>> add_five_to_list()
[5, 5]
>>> # We see that the original `my_list` is still being modified.
>>> add_five_to_list()
[5, 5, 5]
```

If you need to use a mutable type, like a `list` as a default, use a *marker* instead. We'll cover this technique when we talk about `list`s in the next chapter.

In Python, default arguments are evaluated only once -- when the function is defined. Not each time the function is called. That means if you use a value that can be changed, it won't behave like you'd expect it to.

### Naming Functions and Arguments

Because Python is a dynamic language (sometimes called duck-typed) we use names as cues for what our function does, the arguments it accepts, and the values it returns.

This is especially important because we generally don't declare *types* for our programs when we're first starting out. *Note: Python does support Type hinting, but it's more of an intermediate feature. Make sure you have the basics down before learning more about it.*

{{% notice tip %}}
Try to avoid single character names for your functions and variables, unless they have meaning in math.
{{% /notice %}}

For example, in this function, `x` and `y` are common names used when referring to points, so it's OK to use single-letter names in this scenario.

```python
def add_points(x1, y1, x2, y2):
    return x1 + x2, y1 + y2
```

For sequences, like `list`s, it's appropriate to name them in the plural.

For example, I'd expect a variable called `name` to be a single string, and a variable called `names` to be a list of strings.

{{% notice tip %}}
A great resource to help you figure out the best naming conventions to use in your production Python code is a talk by Brandon Rhodes, called ["The Naming of Ducks: Where Dynamic Types Meet Smart Conventions"](https://www.youtube.com/watch?v=YklKUuDpX5c).
{{% /notice %}}
