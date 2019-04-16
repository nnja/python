---
title: "Accepting User Input"
date: 2019-03-10T19:27:09-07:00
draft: false
weight: 3
---

### Accepting Command Line Arguments

To accept basic arguments from the command line, we can use `sys.argv`. `argv` is a list that gets passed in to your program that contains whatever arguments your program was started with. Start a new Python file called `cli_exercise.py` and enter the following:

```python
import sys

args = sys.argv

print(args)
```

Now run it:

```bash
(env) $ python cli_exercise.py
['cli_exercise.py']
```

You should see a list with one item: the name of your program. Pass in additional arguments by adding them after your program name on the command line, separated by spaces:

```bash
python cli_exercise.py argument1 argument2 "hello world"
['cli_exercise.py', 'argument1', 'argument2', 'hello world']
```

Note that the name of the file you're running is rarely useful, so it's common to see this omitted with using slices, for example `sys.argv[1:]`

{{% notice warning %}}
`sys.argv` is never empty - the first element in the list will always be the name of the Python file you're running.
{{% /notice %}}


### Accepting User Input with `input`

You can also accept user data inside a running program by using `input()`. Let's make a simple interactive command line program that asks for a user's name and birthday:

```python
name = input("Hello, what is your name? ")

birthday_string = input(f"Hello {name}. Please enter your birthday in MM/DD/YYYY format: ")

print(f"Hello {name}. Your birthday is on {birthday_string}.")
```

```bash
(env) $ python cli_exercise.py
Hello, what is your name? Floyd
Hello Floyd. Please enter your birthday in MM/DD/YYYY format: 01/20/1990
Hello Floyd. Your birthday is on 01/20/1990.
```