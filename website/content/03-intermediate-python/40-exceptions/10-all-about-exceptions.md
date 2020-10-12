---
title: "All About Exceptions"
date: 2019-03-10T19:15:54-07:00
draft: false
weight: 1
---

Built-in exceptions and easy exception handling is one of the shining features of Python. Technically, errors that happen during parsing are called `SyntaxError`s - these will probably be the most common errors you see, and usually happen because of a mistake in whitespace, a syntax misunderstanding, or a simple typo.

Even if the syntax is correct, errors can still occur when your program is run. We call these Exceptions, and there a many different types (this is a good thing, because the more specifically we know what went wrong, the better we can handle it).

An un-handled exception is fatal: it will print debugging information (called a traceback), stop the interpreter, and exit your program. However, once you learn to handle Exceptions, you can cover your bases and write programs that are robust in the face of issues.


## Types of Exceptions

Python has many useful built-in exceptions that you'll probably encounter in your travels. Some of the more common ones that you'll run into are:

|Exception|Cause of Error|
|---|---|
|AttributeError|Raised when attribute assignment or reference fails.|
|ImportError|Raised when the imported module is not found.|
|IndexError|Raised when index of a sequence is out of range.|
|KeyError|Raised when a key is not found in a dictionary.|
|KeyboardInterrupt|Raised when the user hits interrupt key (Ctrl+c or delete).|
|NameError|Raised when a variable is not found in local or global scope.|
|SyntaxError|Raised by parser when syntax error is encountered.|
|IndentationError|Raised when there is incorrect indentation.|
|ValueError|Raised when a function gets argument of correct type but improper value.|

You can find a more detailed list of built-in exceptions in the [Python documentation](https://docs.python.org/3/library/exceptions.html).

## Exception Hierarchy

An important thing to know is that exceptions, like everything else in Python, are just objects. They follow an inheritance hierarchy, just like classes do. For example, the `ZeroDivisionError` is a subclass of `ArithmeticError`, which is a subclass of `Exception`, itself a subclass of `BaseException`.

So, if you wanted to catch a divide-by-zero error, you could use `except ZeroDivisionError`. But you could also use `except ArithmeticError`, which would catch not only `ZeroDivisionEror`, but also `OverflowError` and `FloatingPointError`. You could use `except Exception`, but this is not a good idea, as it will catch almost *every* type of error, even ones you weren't expecting. We'll discuss this a bit later. Again, a full chart of the hierarchy for built-in exceptions can be found at the bottom of the (Python documentation)[https://docs.python.org/3/library/exceptions.html#exception-hierarchy].

## Exiting your Program

As we mentioned, exceptions that are allowed to bubble up to the top level (called *unhandled* exceptions) will cause your program to exit. This is generally unwanted - even if an error is unrecoverable, we still want to provide more detailed information about the error for later inspection, or a pretty error for the user if our program is user-facing, and in most cases, we want the program to go back to doing what it was doing.

What if we want our program to stop, though? You may already be familiar with `ctrl-c`, the age-old posix method of sending SIGINT (an interrupt signal) to a program. You may be surprised to know asking your operating system to send SIGINT to Python causes, yes, an exception - `KeyboardInterrupt`. And yes, you can catch `KeyboardInterrupt`, but this will make your program a little harder to kill.

You can also use `sys.exit()` from the built-in `sys` library. It's generally not a good idea to pepper `sys.exit()` around your code, as it makes it harder to control when your program exits, but this can be a handy function for controlling how and when your program exits. By default, `sys.exit()` with no parameters will exit with a `0` return code, which, by posix convention, signals success. You can pass an integer to `sys.exit()` if you'd like to exit with a non-zero return code (usually signaling some sort of failure condition). You can also pass a string to `sys.exit()`, which will get printed to the command line, along with a return code of `1`.

`sys.exit()` generates a `SystemExit` exception, which inherits from the master `BaseException` class, which makes it possible for clean-up handlers (such as `finally` statements) to run.