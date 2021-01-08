#!/usr/bin/python3
""" This module adds two integers together."""


def add_integer(a, b=98):
    """ This module adds two integers together. They must both be floats or ints,
    and they must be cast into ints before adding."""
    if a is None:
        raise TypeError("a must be an integer")
    elif type(a) is not int:
        if type(a) is not float:
            raise TypeError("a must be an integer")
    elif b is not None:
        if type(b) is not int:
            if type(b) is not float:
                raise TypeError("b must be an integer")
    return int(a) + int(b)
