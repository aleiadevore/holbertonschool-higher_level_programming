#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Test cases for max_integer """

    def test_simple_list(self):
        self.assertEqual(max_integer([1, 2, 3]), 3, "Should be 3")

    def test_nothing(self):
        self.assertEqual(max_integer(), None, "Should be None")

    def test_char(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'a', 4])

    def test_large_number(self):
        self.assertEqual(max_integer([99999999999, 1, 2]), 99999999999,
                         "Should be 99999999999")

    def test_small_number(self):
        self.assertEqual(max_integer([-99999999, -100000, -2, 0]), 0,
                         "Should be 0")

if __name__ == '__main__':
    unittest.main()
