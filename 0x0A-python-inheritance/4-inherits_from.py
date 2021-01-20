#!/usr/bin/python3
"""This module creates a function that determines if object is an
instance of an inherited class"""


def inherits_from(obj, a_class):
    """This returns True if obj is instance of a class inherited from
    a_class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
