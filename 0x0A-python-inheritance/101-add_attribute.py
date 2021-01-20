#!/usr/bin/python3
"""This creates a function that adds a new attribute to an object if
it's possible"""


def add_attribute(class_nm, attr, value):
    """This adds an attribute if possible"""
    for elem in dir(class_nm):
        if elem == attr:
            class_nm.attr = value
            return
    raise TypeError("can't add new attribute")
