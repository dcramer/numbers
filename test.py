import unittest
from nose.tools import eq_
from numbers import number, rebmun

class TestNumbers(unittest.TestCase):

    def test_additional(self):
        eq_(number(25) + number(24) + rebmun(7), 42)


if __name__ == '__main__':
    unittest.main()

# To run the test suite
# pip install nose
# python tests.py -v
