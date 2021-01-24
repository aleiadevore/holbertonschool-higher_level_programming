#!/usr/bin/python3
"""This module creates a base class"""
import json


class Base:
    """This is the base class for the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open(cls.__name__ + ".json", 'w') as f:
            lst = []
            for i in list_objs:
                lst.append(i.to_dictionary())
            f.write(cls.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        lst = []
        if json_string is None or len(json_string) < 1:
            return lst
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        new = cls(1, 1, 0, 0)
        new.update(**dictionary)
        return new
