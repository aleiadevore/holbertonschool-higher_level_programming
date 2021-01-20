#!/usr/bin/python3
"""This creates a function that adds a new attribute to a module if
it's possible"""


def add_attribute(class_nm, attr, value):
    for elem in dir(class_nm):
        if elem == attr:
            class_nm.attr = value
            return
    raise TypeError("can't add new attribute")
