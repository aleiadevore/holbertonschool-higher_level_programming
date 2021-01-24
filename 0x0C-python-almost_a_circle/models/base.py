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
