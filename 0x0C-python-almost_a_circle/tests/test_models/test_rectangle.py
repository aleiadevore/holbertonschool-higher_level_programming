#!/usr/bin/python3
"""Unittest for Rectangle class([..])
"""


import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """ Test cases for base class """

    @classmethod
    def setUpClass(cls):
        cls.r1 = Rectangle(1, 1)

    def test_simple_rectangle(self):
        self.assertEqual(self.r1.width, 1, "Should be 1")
        self.assertEqual(self.r1.height, 1, "Should be 1")
        self.assertEqual(self.r1.x, 0, "Should be 0")

    def test_width_error(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 1)

    def test_height_error(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_x_error(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1, 1)

    def test_y_error(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 0, -1)

    @classmethod
    def setUpClass(cls):
        cls.r1 = Rectangle(1, 1)
        cls.r3 = Rectangle(3, 3)

    def test_area(self):
        self.assertEqual(self.r1.area(), 1, "Should be 1")

    def test_area_2(self):
        self.assertEqual(self.r3.area(), 9, "Should be 9")

    def test_none(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle(None)

    def test_dict(self):
        r5 = Rectangle(10, 2, 1, 9, 10)
        r5_dictionary = r5.to_dictionary()
        self.assertEqual(r5_dictionary, {'x': 1, 'y': 9, 'id': 10,
                                         'height': 2, 'width': 10})

if __name__ == '__main__':
    unittest.main()
