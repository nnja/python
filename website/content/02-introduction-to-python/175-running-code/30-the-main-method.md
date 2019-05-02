---
title: "The main Method"
date: 2019-02-10T18:16:47-08:00
draft: false
weight: 30
---

Once you start writing more comprehensive Python programs, you'll want to include a `main` method in your code.

The purpose of checking for the `main` method is to make sure that the code in your `main` method is only run when it's executed as a stand-alone program. Because of how Python's import system works, if someone else imports your Python program, any code in it is executed on import.

We'll talk more about imports and modules on day two, but let's look at a quick example.

Let's say we had a Python file named `name_lib.py`

```python
def name_length(name):
    return len(name)

def upper_case_name(name):
    return name.upper()

def lower_case_name(name):
    return name.lower()

name = "Nina"
length = name_length(name)
upper_case = upper_case_name(name)

print(f"The length is {length} and the uppercase version is: {upper_case}")
```

If we ran this code, we'd see exactly what we expect.

```bash
(env) $ python name_lib.py
name_lib.py
The length is 4 and the uppercase version is: NINA
```

### Writing Reusable Code

We went through all this trouble of writing a useful name library. What if someone else wanted to use our library in their own code by `import`ing it?

Let's say someone else wrote their own program, in `other_program.py`

```python
import name_lib

my_name = "Fred"

my_length = name_lib.name_length(my_name)
my_lower_case = name_lib.lower_case_name(my_name)

print(f"In my code, my length is {my_length} and my lower case name is: {my_lower_case}")
```

If we ran this, we'd see the following result:

```bash
(env) $ python other_program.py

The length is 4 and the uppercase version is: NINA
In my code, my length is 4 and my lower case name is: fred
```

If I'm Fred, I just wanted to use this cool library. But all of a sudden, I'm seeing information about Nina!

To prevent this from happening, we want to write a conditional that will only run *our* code if we're the ones running the program directly.

To do that, we'll need to check if `__name__ == __main__`.

Let's unwrap that.

`__name__` is a special variable that's set by Python that tells it where it was called from. We can tell it's a special variable because it starts and ends with `__`. That's a hint that you don't want to *change* the value of this variable, or it could adversely affect the execution of your Python program.

{{% notice tip %}}
In Python, `__` is also called double underscore, or *dunder*.
{{% /notice %}}

Let's comment out our original `print`, and add the following line to the end of `name_lib.py`:

```python
# Note: add to the bottom of name_lib.py

# print(f"The length is {length} and the uppercase version is: {upper_case}")
print(f"The value of __name__ is: {__name__}")
```

Now, let's run `name_lib.py` again. We should see:

```bash
(env) $ python name_lib.py
The value of __name__ is: __main__
```

We're getting somewhere. When we run this file directly, we'll see that `__name__` has the *value* of `__main__`.

What if we run our other program again?

```bash
(env) $ python other_program.py
The value of __name__ is: name_lib
```

When we "run" our library by importing it, we'll see that it's `__name__` is set to the name of the file that it's in, minus the `.py` extension. In this case, `__name__` is set to `name_lib`.

### Putting Code in a `main` Conditional

To avoid running our code when it's imported by other modules, we put it in a conditional statement, and explicitly check `if __name__ == "__main__"`.

Let's update `name_lib.py`, and put our own code inside of the conditional check.

```python
def name_length(name):
    return len(name)

def upper_case_name(name):
    return name.upper()

def lower_case_name(name):
    return name.lower()

if __name__ == "__main__":
    name = "Nina"
    length = name_length(name)
    upper_case = upper_case_name(name)

    print(f"The length is {length} and the uppercase version is: {upper_case}")
```

Now, if we run `other_program.py`, we'll see:

```bash
(env) $ python other_program.py
In my code, my length is 4 and my lower case name is: fred
```

Much better!

{{% notice note %}}
Using a `main` method is a common pattern that you’ll see in Python programs, and it comes in handy for being able to write programs that work both on their own and when imported into other programs.
{{% /notice %}}

