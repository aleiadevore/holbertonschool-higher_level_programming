#!/usr/bin/python3
"""Returns True if object is exactly an instance of the
specified class"""


def is_same_class(obj, a_class):
    """Returns if classes are the same"""
    return type(obj) is a_class
