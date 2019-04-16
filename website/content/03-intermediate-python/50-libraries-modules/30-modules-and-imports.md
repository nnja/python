---
title: "Modules and Imports"
date: 2019-03-10T19:16:35-07:00
draft: false
weight: 3
---

Python has a simple package structure. Any directory with a file named `__init__.py` can be considered a Python module.

{{% notice info %}}
Note: a `__init__.py` file is no longer *required* for Python 3 modules, but it's still supported and can be useful.
{{% /notice %}}

For example, let's make a basic function and start a new module to house it:

```python
def add_numbers(x, y):
    return x + y
```

Let's put our function in a file called `__init__.py` and place it in a folder called `my_math_functions`. Now, as long as the folder `my_math_functions` is somewhere in our `PYTHONPATH`, we can `import my_math_functions` and reach `add_numbers()`. If we start our REPL from the folder that contains `my_math_functions`, we can import it:

```python
>>> import my_math_functions
>>> my_math_functions.add_numbers(1, 2)
3
```

### Best Practices

There a few different ways to import modules or even just specific objects from modules. You can import *everything* from a module into the local namespace using `*`:

```python
>>> from my_math_functions import *
>>> add_numbers(1, 2)
3
```

This isn't a good practice, because it's hard to tell where a specific function is coming from without the namespace context. Also, function names can conflict, and this can make things very difficult to debug.

Better is to import functions specifically:

```python
>>> from my_math_functions import add_numbers
>>> add_numbers(1, 2)
3
```

This make things a little clearer, as we can look at the top and see where the `add_number()` function came from. However, an even better way is to just import the module and use it in calls to maintain the namespace context:

```python
>>> import my_math_functions
>>> my_math_functions.add_numbers(1, 2)
3
```

This can be slightly more verbose, but unless it makes your function calls ridiculously long, it generally makes things much easier to debug.

{{% notice tip %}}
You can use the `as` keyword to make things a little easier on yourself.
{{% /notice %}}

```python
>>> import my_math_functions as mmf
>>> mmf.add_numbers(1, 2)
3
```

### PYTHONPATH

What is the `PYTHONPATH` we mentioned earlier? This is a list of paths on your system where Python will look for packages. Python will always look first in the working directory (the folder you're in when you start the REPL or run your program), so if your module folder is there, you can import it. You can also install your modules just like any other external modules, using a `setup.py` file. It's also possible to change or add paths to your `PYTHONPATH` list if you need to store modules elsewhere, but this isn't a very portable solution.