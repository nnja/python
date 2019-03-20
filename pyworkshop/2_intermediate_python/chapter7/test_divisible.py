import unittest
from divisible import divisible_by

class TestCase(unittest.TestCase):

    def test_divisible_by(self):
        self.assertTrue(divisible_by(10, 2))
        self.assertTrue(divisible_by(10, 3))


if __name__ == '__main__':
    unittest.main()
