#!/usr/bin/python3
"""Unittest for Square class([..])
"""


import unittest
from models.square import Square


class TestBase(unittest.TestCase):
    """ Test cases for Square class """

    @classmethod
    def setUpClass(cls):
        cls.s1 = Square(1)

    def test_simple_rectangle(self):
        self.assertEqual(self.s1.width, 1, "Should be 1")
        self.assertEqual(self.s1.height, 1, "Should be 1")
        self.assertEqual(self.s1.x, 0, "Should be 0")

if __name__ == '__main__':
    unittest.main()
