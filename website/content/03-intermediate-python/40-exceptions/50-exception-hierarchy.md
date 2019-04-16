---
title: "Exception Hierarchy"
date: 2019-03-10T19:15:44-07:00
draft: true
weight: 5
---

Python has many useful built-in exceptions that you'll probably encounter in your travels. Some of the more common ones that you'll run into are listed in the [All About Exceptions](../10-all-about-exceptions) section. You can find a more detailed list of built-in exceptions in the [Python documentation](https://docs.python.org/3/library/exceptions.html).

An important thing to know is that exceptions, like everything else in Python, are just objects. They follow an inheritance hierarchy, just like classes do. For example, the `ZeroDivisionError` is a subclass of `ArithmeticError`, which is a subclass of `Exception`, itself a subclass of `BaseException`.

```python
>>> issubclass(ZeroDivisionError, ArithmeticError)
True
>>> issubclass(ArithmeticError, Exception)
True
>>> issubclass(Exception, BaseException)
True

# Thus,
>>> issubclass(ZeroDivisionError, BaseException)
True
```

So, if you wanted to catch a divide-by-zero error, you could use `except ZeroDivisionError`. But you could also use `except ArithmeticError`, which would catch not only `ZeroDivisionEror`, but also `OverflowError` and `FloatingPointError`. You could use `except Exception`, but this is not a good idea, as it will catch almost *every* type of error, even ones you weren't expecting. We'll discuss this a bit later.

A full chart of the hierarchy for built-in exceptions can be found at the bottom of the [Python documentation](https://docs.python.org/3/library/exceptions.html#exception-hierarchy).