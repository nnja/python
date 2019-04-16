---
title: "Function Scope"
date: 2019-02-10T18:30:11-08:00
draft: false
weight: 40
---

### Scope inside a function

Inside of a function in Python, the **scope** changes.

Think about it this way: scoping in Python happens with whitespace. When we delineate the code a function contains by indenting it under a function definition, it's scope **changes** to a new internal scope. It has access to the variables defined outside of it, but it can't change them.

Once the function is done running, its scope goes away, as do its defined variables.

Let's double check this in the REPL:

```python
>>> def twitter_info():
...     twitter_account = "nnja"
...     print(f"Account inside function: {twitter_account}")
...
>>> twitter_info()
Account inside function: nnja
>>> print(f"Account outside of function: {twitter_account}")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'twitter_account' is not defined
```

We get a `NameError` when trying to access the `twitter_account` variable outside of the function. That's because it's out of scope, exactly like we expected it to be.


### Using variables defined outside of the function

Generally, we want to be careful when using variables defined outside of our function.

Note, that if we try to change the value of a variable defined outside of our function, we'll see the changes in the function, but not outside of it.

You can't change variables defined outside of the function inside of the function. If you try to, your changes will only apply while the function is running. Once the function is done running, the value goes back to what it was before your function ran.

A little confusing, but let's see it in action:

```python
>>> name = "Nina"
>>> print(f"Name outside of function: {name}")
Name outside of function: Nina
>>>
>>> def try_change_name():
...     name = "Max"
...     print(f"Name inside of function: {name}")
...
>>> try_change_name()
Name inside of function: Max
>>> print(f"Name outside of function: {name}")
Name outside of function: Nina
```

If we didn't know what to look for, the program might not behave how we'd expect it to. A good rule of thumb is to name our variables clearly, and minimize how many variables we declare outside of functions and classes, which you'll learn about in day two.


{{% notice tip %}}
An appropriate use is when using a constant, a variable defined in all caps, with the words separated by underscores. A constant is a value that we expect to use several times within our program, but we never expect to change it programmatically.
{{% /notice %}}

For example:

```python
>>> ROOT_API_URL =  "https://api.github.com"
>>> def api_search_repos_url():
...     return f"{ROOT_API_URL}/search/repositories"
...
>>> api_search_repos_url()
'https://api.github.com/search/repositories'
>>>
```