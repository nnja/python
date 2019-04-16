---
title: "Writing Tests"
date: 2019-03-10T19:30:36-07:00
draft: false
weight: 5
---

There are a few different frameworks for writing unit tests in Python, but they're all very similar. We'll focus on the built-in `unittest` library. `unittest` is both a framework for writing tests, as well as a test runner, meaning it can execute your tests and return the results. In order to write `unittest` tests, you must:

* Write your tests as methods within classes
* Use a series of built-in assertion methods

Let's start with a simple function to test, `multiply()`, which takes two numbers and multiplies them.

```python
def multiply(x, y):
    return x * y
```

Easy enough. Let's write a test case for it. Usually this will be broken out into a separate file, but we'll combine them for this contrived example. We'll create a `TestMultiply` class that derives from `unittest.TestCase`, with a method inside that does the actual testing. Lastly, we'll call `unittest.main()` to tell `unittest` to find and run our TestCase. We'll put all this in a file called `test_multiply.py` and run it from the command line:

```python
import unittest

def multiply(x, y):
    return x * y

class TestMultiply(unittest.TestCase):

    def test_multiply(self):
        test_x = 5
        test_y = 10
        self.assertEqual(multiply(test_x, test_y), 50, "Should be 50")

if __name__ == "__main__":
    unittest.main()
```

```bash
(env) $ python test_multiply.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

### Failing Tests

Let's introduce a bug into our `multiply()` function and see what happens when we run the test:

```python
import unittest

def multiply(x, y):
    return x * x

class TestMultiply(unittest.TestCase):

    def test_multiply(self):
        test_x = 5
        test_y = 10
        self.assertEqual(multiply(test_x, test_y), 50, "Should be 50")

if __name__ == "__main__":
    unittest.main()
```

```bash
(env) $ python test_multiply.py
F
======================================================================
FAIL: test_multiply (__main__.TestMultiply)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_multiply.py", line 11, in test_multiply
    self.assertEqual(multiply(test_x, test_y), 50, "Should be 50")
AssertionError: 25 != 50 : Should be 50

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
```

### Important Concepts

* `TestCase` class must subclass `unittest.TestCase`
* Names of test functions must begin with `test_`
* Import the code to be tested

Your `TestCase` class can be called whatever you want, but you must subclass `unittest.TestCase` in order for it to work.

{{% notice info %}}
Your test functions in your TestCase must begin with `test_`, otherwise they won't be run as tests.
{{% /notice %}}

This can be useful if you need to include utility functions inside your TestCase.

Lastly, your test code will need access to your code to be tested. For a small project, this is easily done by putting your tests in a `test.py` file alongside your code. For larger projects, you usually want to have multiple test files inside a `test` folder. In this case, you'll need to make sure your code to be tested is available on your `PYTHONPATH`.

### Running your Tests

As we saw, one common way of running your tests is by calling `unittest.main()`:

```python
if __name__ == "__main__":
    unittest.main()
```

Add this to your test file, run it, and you're off to the races. You can also skip this bit, and call `unittest` directly from the command line:

```bash
(env) $ python -m unittest test_module
```

Here, you don't need to make your test file runnable (by using `unittest.main()`), instead you're running `unittest` directly and telling it where to find your tests.

{{% notice tip %}}
Use the `-v` (or `--verbose`) flag can give you more information about which tests were run
{{% /notice %}}


```bash
(env) $ python -m unittest test_multiply -v
test_multiply (test_multiply.TestMultiply) ... FAIL

======================================================================
FAIL: test_multiply (test_multiply.TestMultiply)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/nina/Desktop/test_multiply.py", line 11, in test_multiply
    self.assertEqual(multiply(test_x, test_y), 50, "Should be 50")
AssertionError: 25 != 50 : Should be 50

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
```


### TestCase Assertions

Subclassing the TestCase class gives you a bunch of useful assertions that you can use to check the validity of your code. Here's the list from the [Python documentation](https://docs.python.org/3/library/unittest.html):


|Method|Checks that|
|---|---|
|assertEqual(a, b)|a == b|
|assertNotEqual(a, b)|a != b|
|assertTrue(x)|bool(x) is True|
|assertFalse(x)|bool(x) is False|
|assertIs(a, b)|a is b|
|assertIsNot(a, b)|a is not b|
|assertIsNone(x)|x is None|
|assertIsNotNone(x)|x is not None|
|assertIn(a, b)|a in b|
|assertNotIn(a, b)|a not in b|
|assertIsInstance(a, b)|isinstance(a, b)|
|assertNotIsInstance(a, b)|not isinstance(a, b)|


### Growing your Tests

Standard `unittest` tests are fine for most projects. As your programs grow and organization becomes more complex, you might want to consider an alternative testing framework or test runner. The 3rd party `nose2` and `pytest` modules are compatible with `unittest` but do things slightly differently. You can find more information in the [nose2 documentation](https://nose2.readthedocs.io/en/latest/) and [pytest documentation](https://docs.pytest.org/en/latest/).