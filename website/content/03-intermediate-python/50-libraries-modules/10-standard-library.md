---
title: "Standard Library"
date: 2019-03-10T19:16:56-07:00
draft: false
weight: 1
---

Python has always had a "batteries included" philosophy - having a rich and versatile standard library which is immediately available, without making the user download separate packages. This is thought to have contributed to Python's early success. No matter what you're trying to accomplish, there's probably a built-in library that can help you do what you want.

The downside to this is that the standard libraries need to maintain backwards compatibility. Some were quick hacks, hard to use, poorly designed and now impossible to fix, or have simply been rendered obsolete. Luckily, Python also makes it easy to install and use external libraries - we'll cover this later.


### The Standard Library

There are some great libraries included with Python that you'll probably end up seeing or using frequently. `sys` provides system-specific parameters and functions, such as `exit()`. `os` has miscellaneous operating system interfaces, and provides the excellent `os.path` submodule for handling file paths on any operating system. `math` gives you all the advanced math function. `json` is an easy-to-use json parser and encoder. Python even gives you built-in libraries for database access, logging, internet protocols, multimedia, debugging, and even libraries for extending Python itself. The full list of standard libraries can be found in the [Python documentation](https://docs.python.org/3/library/).

As a quick example, let's look at Python's `datetime` library. You can easily make a `datetime` object that represents any given point in time. For example:

```python
>>> import datetime
>>> right_now = datetime.datetime.now()
>>> print(right_now)
2019-03-17 13:41:10.994700
>>> repr(right_now)
'datetime.datetime(2019, 3, 17, 13, 41, 10, 994700)'
```

We can even make a `datetime` object for an arbitrary date, and subtract it from right now to get a `timedelta` object:

```python
>>> new_years = datetime.datetime(2019, 1, 1, 0, 0)
>>> print(new_years)
2019-01-01 00:00:00
>>> delta = right_now - new_years
>>> print(delta)
75 days, 13:41:10.994700
```

We can easily see that it's been over 75 days from `new_years` until `right_now`. We'll come back to `datetime` later in this chapter.