#!/usr/bin/python3
"""This module creates a function that writes into a file"""


def append_write(filename="", text=""):
    """Creates a file if it doesn't exist, writes text, and appends to
    existing text"""

    with open(filename, 'a') as f:
        a = f.write(text)
    f.close
    return a
