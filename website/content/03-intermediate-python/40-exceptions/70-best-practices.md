---
title: "Best Practices"
date: 2019-03-10T19:15:44-07:00
draft: false
weight: 7
---

### Catch More Specific Exceptions First

Remember, your `except` handlers are evaluated in order, so be sure to put more specific exceptions first. For example:

```python
>>> try:
...     my_value = 3.14 / 0
... except ArithmeticError:
...     print("We had a general math error")
... except ZeroDivisionEror:
...     print("We had a divide-by-zero error")
...
We had a general math error
```

When we tried to divide by zero, we inadvertently raised a ZeroDivisionError. However, because ZeroDivisionError is a subclass of ArithmeticError, and `except ArithemticError` came first, the information about our specific error was swallowed by the `except ArithemticError` handler, and we lost more detailed information about our error.

### Don't Catch `Exception`

It's bad form to catch the general `Exception` class. This will catch every type of exception that subclasses the `Exception` class, which is almost all of them. You may have errors that you don't care about, and don't affect the operation of your program, or maybe you're dealing with a flaky API and want to swallow errors and retry. By catching `Exception`, you run the risk of hitting an unexpected exception that your program actually can't recover from, or worse, swallowing an important exception without properly logging it - a huge headache when trying to debug programs that are failing in weird ways.


### Definitely don't catch `BaseException`

Catching `BaseException` is a really bad idea, because you'll swallow every type of Exception, including `KeyboardInterrupt`, the exception that causes your program to exit when you send a SIGINT (Ctrl-C). Don't do it.