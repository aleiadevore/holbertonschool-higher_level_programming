#!/usr/bin/python3
"""This module creates a function that writes into a file"""


def write_file(filename="", text=""):
    """Creates a file if it doesn't exist, writes text, and overrides
    existing text"""

    with open(filename, 'w') as f:
        a = f.write(text)
    f.close
    return a
