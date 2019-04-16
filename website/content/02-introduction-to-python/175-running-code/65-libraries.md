+++
title = "Working with Libraries"
date = 2019-01-25T15:06:06-06:00
weight = 65
draft = false
+++

Working with external libraries in Python makes use of the `import` keyword. While this can go anywhere in your file, it's almost always best to import libraries at the top of each file where they're used. For example, in the last section, we were able to call upon the built-in `json` library by calling `import json` at the top of our code.

Importing modules with the `import` keyword is usually the best method, because it preserves the module's namespace. However, you can also use the `from <module> import <object>` syntax to import a specific object (function, variable, subclass, etc.) from a module into your program's namespace.

For example, if we wanted a random integer between 0 and 100, we could use `random.randint()`:

```python
>>> import random
>>> random.randint(0, 100)
42
```

Notice that the namespace is preserved (we needed to call `random.randint()`). If we use `from` instead:

```python
>>> from random import randint
>>> randint(0, 100)
64
```


### Installing the requests library with `pip`

For the next chapter, we'll be using an excellent 3rd part library called `requests` to make light work of retrieving data from web APIs. To install the `requests` library, run this on your command line:

```bash
(env) $ python -m pip install requests
```

This runs the `pip` module and asks it to find the `requests` library on PyPI.org (the Python Package Index) and install it in your local system, so that it becomes available for you to import. We'll dive a little more into this later.