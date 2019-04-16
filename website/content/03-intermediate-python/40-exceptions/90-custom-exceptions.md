---
title: "Custom Exceptions"
date: 2019-03-10T19:16:01-07:00
draft: false
weight: 9
---

As we mentioned, exceptions are just regular classes that inherit from the `Exception` class. This makes it super easy to create our own custom exceptions, which can make our programs easier to follow and more readable. An exception need not be complicated, just inherit from `Exception`:

```python
>>> class MyCustomException(Exception):
...     pass
...
>>> raise MyCustomException()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyCustomException
```

It's OK to have a custom `Exception` subclass that only `pass`-es - your exception doesn't need to do anything fancy to be useful. Having custom exceptions - tailored to your specific use cases and that you can raise and catch in specific circumstances - can make your code much more readable and robust, and reduce the amount of code you write later to try and figure out what exactly went wrong.

Of course, you can get as fancy as you want. You can send additional information, like messages, to your exceptions. Just add an `__init__()` method to your exception class, with whatever arguments you want.

```python
class IncorrectValueError(Exception):
...     def __init__(self, value):
...         message = f"Got an incorrect value of {value}"
...         super().__init__(message)
...
>>> my_value = 9999
>>> if my_value > 100:
...     raise IncorrectValueError(my_value)
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
__main__.IncorrectValueError: Got an incorrect value of 9999
```

`Exception` takes an optional string argument message that gets printed with your exception. We pass our erroneous value to our `IncorrectValueError` object, which constructs a special message and passes it its parent class, `Exception`, via `super().__init__()`. The custom message string, along with the value for context, gets printed along with our error traceback.

### A Custom Exception for our GitHub API app

If we wanted to write a custom Exception for our GitHub API app, it might look something like this.

```python
class GitHubApiException(Exception):

    def __init__(self, status_code):
        if status_code == 403:
            message = "Rate limit reached. Please wait a minute and try again."
        else:
            message = f"HTTP Status Code was: {status_code}."

        super().__init__(message)
```

Notice how it takes the HTTP status code into account, and displays a custom error message for the 403, rate limited reached status code.