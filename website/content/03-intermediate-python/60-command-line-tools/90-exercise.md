+++
title = "Practice"
date = 2019-01-25T15:07:04-06:00
weight = 200
draft = false
pre = "<b>⭐️ </b>"
+++

## Accepting User Input with Args

To accept basic arguments from the command line, we can use `sys.argv`. Start a new Python file called `cli_exercise.py` and enter the following.

```python
import sys

args = sys.argv

print(args)
```

Then, run it from the command line:

```bash
(env) $ python cli_exercise.py
```


{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python cli_exercise.py
['cli_exercise.py']
```
{{% /expand%}}

You should see a list with one item: the name of your program. Pass in additional arguments by adding them after your program name on the command line, separated by spaces:

```bash
(env) $ python cli_exercise.py argument1 argument2 "hello world"
```

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python cli_exercise.py argument1 argument2 "hello world"
['cli_exercise.py', 'argument1', 'argument2', 'hello world']
```

{{% /expand%}}

Note that the name of the file you're running is rarely useful, so it's common to see this omitted with using slices, for example `sys.argv[1:]`

## Accepting User Input with `input`

You can also accept user data inside a running program by using `input()`. Let's make a simple interactive command line program that asks for a user's name and birthday. Call it `cli_exercise_input.py`. Use `input()` to get the user's name and birthday, and greet the user (call `strip()` on their name to remove any extra whitespace).

{{%expand "You should have written something like this:" %}}

```python
name = input("Hello, what is your name? ")

birthday_string = input(f"Hello {name.strip()}. Please enter your birthday in MM/DD/YYYY format: ")

print(f"Hello {name}. Your birthday is on {birthday_string}.")
```
{{% /expand%}}

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python cli_exercise_input.py
Hello, what is your name? Floyd
Hello Nina. Please enter your birthday in MM/DD/YYYY format: 01/20/1990
Hello Floyd. Your birthday is on 01/20/1990.
```

{{% /expand%}}

### Optional Advanced Exercise

{{% notice note %}}
If you thought this exercise was a breeze, try this optional advanced exercises.
{{% /notice %}}


Refactor the final exercise from Intro to Python, using custom exceptions and a class to store the information about a GitHub Repo. Accept the list of languages as user input.

You can see an example implementation in the repo for this course at [git.io/python3](https://git.io/python3)