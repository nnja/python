+++
title = "Practice"
date = 2019-01-25T15:07:04-06:00
weight = 10
draft = false
pre = "<b>⭐️ </b>"
+++

## Tests

Python comes with a very easy-to-use `unittest` library built in. Write a simple function that accepts two numbers, and returns `True` if the first number is evenly divisible by the second.

```python
def divisible_by(check_number, divisor):
    return check_number % divisor == 0
```

Save your file as `divisible.py`. In a second file called `test_divisible.py`, create a `TestCase` using the `unittest` framework and use asserts to verify that the `divisible_by()`function returns the correct result. Don't forget to import your `divisible_by()` function.

```python
import unittest
from divisible import divisible_by

class TestCase(unittest.TestCase):

    def test_divisible_by(self):
        self.assertTrue(divisible_by(10, 2))
        self.assertTrue(divisible_by(10, 3))


if __name__ == '__main__':
    unittest.main()
```

Name your file `test_divisible.py` and run it:

```bash
(env) $ python test_divisible.py --verbose
```

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python test_divisible.py --verbose
test_divisible_by (__main__.TestCase) ... FAIL

======================================================================
FAIL: test_divisible_by (__main__.TestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_divisible.py", line 8, in test_divisible_by
    self.assertTrue(divisible_by(10, 3))
AssertionError: False is not true

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
```
{{% /expand%}}

You should have gotten an error: `AssertionError: False is not true` caused by `self.assertTrue(divisible_by(10, 3))`. Makes sense, because 10 is not evenly divisible by 3.

{{% notice tip %}}
Change `self.assertTrue` to `self.assertFalse` and your test should pass.
{{% /notice %}}

```bash
(env) $ python test_divisible.py --verbose
test_divisible_by (__main__.TestCase) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```