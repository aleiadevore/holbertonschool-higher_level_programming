#!/usr/bin/python3
"""Creates a function that determines if object is an instance of or
inherited instance of a class"""


def is_kind_of_class(obj, a_class):
    """This function returns True if obj is instance of a_class or an instance of
    a class inherited from a_class"""
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
