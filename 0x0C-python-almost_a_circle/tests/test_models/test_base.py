#!/usr/bin/python3
"""Unittest for Base class([..])
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test cases for base class """

    @classmethod
    def setUpClass(cls):
        cls.b1 = Base()
        cls.b2 = Base()

    def test_simple_id(self):
        self.assertEqual(self.b2.id, 2, "Should be 2")

    @classmethod
    def setUpClass(cls):
        cls.b1 = Base()
        cls.b2 = Base()
        cls.b3 = Base(4)

    def test_rename_id(self):
        self.assertEqual(self.b3.id, 4, "Should be 4")

if __name__ == '__main__':
    unittest.main()
