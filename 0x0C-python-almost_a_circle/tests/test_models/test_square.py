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

    def test_simple_square(self):
        self.assertEqual(self.s1.width, 1, "Should be 1")
        self.assertEqual(self.s1.height, 1, "Should be 1")
        self.assertEqual(self.s1.x, 0, "Should be 0")

    def test_none(self):
        with self.assertRaises(TypeError):
            s2 = Square(None)

    def test_size_error(self):
        with self.assertRaises(ValueError):
            Square(0, 1)

    def test_x_error(self):
        with self.assertRaises(ValueError):
            Square(1, -1)

    def test_y_error(self):
        with self.assertRaises(ValueError):
            Square(1, 1, -1)

    def test_area(self):
        s3 = Square(1)
        self.assertEqual(s3.area(), 1, "Should be 1")

    def test_area(self):
        s4 = Square(3)
        self.assertEqual(s4.area(), 9, "Should be 9")

    def test_dict(self):
        s6 = Square(10, 2, 1, 9)
        s6.id = 10
        s6_dict = s6.to_dictionary()
        self.assertEqual(s6_dict, {'y': 1, 'size': 10, 'id': 10, 'x': 2})

if __name__ == '__main__':
    unittest.main()
