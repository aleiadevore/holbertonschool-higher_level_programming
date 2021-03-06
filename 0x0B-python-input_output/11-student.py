#!/usr/bin/python3
"""This module creates a student class"""


class Student:
    """Creates a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        d = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            for j in self.__dict__:
                if i == j:
                    if i == "first_name":
                        d[i] = self.first_name
                    elif i == "last_name":
                        d[i] = self.last_name
                    else:
                        d[i] = self.age
        return d

    def reload_from_json(self, json):
        if json is not None:
            self.__dict__ = json
