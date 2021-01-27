#!/usr/bin/python3
"""Unittest for Base class([..])
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


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

    def test_to_JSON(self):
        r1 = Rectangle(10, 7, 2, 8, 6)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(dictionary, {'height': 7, 'width': 10, 'id': 6,
                                      'x': 2, 'y': 8})
        self.assertIs(type(json_dictionary), str)

    def test_JSON_to_file_success(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            for line in file:
                self.assertIs(type(line), str)

    def test_JSON_to_dict_empty(self):
        list_output = Rectangle.from_json_string("")
        self.assertEqual(list_output, [])

    def test_JSON_to_dict(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'id': 89, 'width': 10, 'height': 4},
                                       {'id': 7, 'width': 1, 'height': 7}])

    def test_dict_to_inst_success(self):
        r1 = Rectangle(3, 5, 1, 0, 4)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r2.__str__(), "[Rectangle] (4) 1/0 - 3/5")

if __name__ == '__main__':
    unittest.main()
