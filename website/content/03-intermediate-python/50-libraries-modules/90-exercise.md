+++
title = "Practice"
date = 2019-01-25T15:07:04-06:00
weight = 10
draft = false
pre = "<b>⭐️ </b>"
+++

## The Standard Library

The Python standard library has a huge number of packages - no matter what you want to do, there's probably a package included. Let's practice using some of the more common ones. Create a new file and use the `os` module to see if you can get a file listing for the folder your new file is in.

```python
import os

my_folder = os.getcwd()
print(f"Here are the files in {my_folder}:")

with os.scandir(my_folder) as folder:
    for entry in folder:
        print(f" - {entry.name}")
```

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python libraries_exercise.py
Here are the files in /Users/nina/Desktop/libraries_exercise:
 - libraries_exercise.py
```

{{% /expand%}}

`sys` is another commonly useful library, giving you access to some variables and functions used or maintained by the Python interpreter. Let's try using `sys` to get the arguments passed into our program from the command line, and to figure out what kind of computer we're using:

```python
import sys

arguments = sys.argv
print(f"We received the following arguments:")

for arg in arguments:
    print(f" - {arg}")

print(f"We are running on a '{sys.platform}' machine")
```

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python libraries_exercise.py argument1 hello world "this is one argument"
We received the following arguments:
 - libraries_exercise.py
 - argument1
 - hello
 - world
 - this is one argument
We are running on a 'darwin' machine
```
Note: if the string returned by `sys.platform` isn't what you expect, take a look at the [sys documentation](https://docs.python.org/3/library/sys.html).

{{% /expand%}}

## Pypi

PyPI (the Python Package Index) is an awesome service that helps you find and install almost any 3rd party Python package. You can browse the site at [PyPI.org](https://PyPI.org/) but most of the time you will probably interact with it through Python's `pip` command line tool.

For example, earlier you may have installed the `requests` module. If you search `pip` for `requests`, you'll see every package in the index containing the word requests:

```bash
(env) $ python -m pip search requests
requests-hawk (1.0.0)                  - requests-hawk
requests-dump (0.1.3)                  - `requests-dump` provides hook functions for requests.
requests-aws4auth (0.9)                - AWS4 authentication for Requests
...
```

We just want the one named `requests`, so we'll install it with the `install` keyword. If you don't have it installed, `pip` will install it for you. If you installed it earlier, you'll see something like this:

```bash
(env) $ python -m pip install requests
Requirement already satisfied: requests in /usr/local/lib/python3.7/site-packages (2.21.0)
Requirement already satisfied: chardet<3.1.0,>=3.0.2 in /usr/local/lib/python3.7/site-packages (from requests) (3.0.4)
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/site-packages (from requests) (2019.3.9)
Requirement already satisfied: idna<2.9,>=2.5 in /usr/local/lib/python3.7/site-packages (from requests) (2.8)
Requirement already satisfied: urllib3<1.25,>=1.21.1 in /usr/local/lib/python3.7/site-packages (from requests) (1.24.1)
```