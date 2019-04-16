---
title: "Assertions"
date: 2019-03-10T19:30:41-07:00
draft: false
weight: 3
---

Python comes with a handy-dandy `assert` keyword that you can use for simple sanity checks. An assertion is simply a boolean expression that checks if its conditions return true or not. If the assertion is true, the program continues. If it's false, it throws an `AssertionError`, and your program will stop. Assertions are also a great debugging tool, as they can stop your program in exactly the spot where an error has occurred. This is great for rooting out unreliable data or faulty assumptions.

To make an assertion, just use the `assert` keyword followed by a condition that should be `True`:

```python
>>> input_value = 25
>>> assert input_value > 0
```

If our assertion fails, however:

```python
>>> input_value = 25
>>> assert input_value > 100
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```

### `assert` Is For Sanity Checks, Not For Production!

Assertions are great for simple self-checks and sanity tests. You shouldn't, however, use assertions for failure cases that can occur because of bad user input or operating system/environment failures, such as a file not being found. These situations are much better suited to an exception or an error message.

{{% notice warning %}}
Assertions can be disabled at run time, by starting the program with `python -O`, so you shouldn't rely on assertions to run in production code. Don't use them for validation!
{{% /notice %}}
