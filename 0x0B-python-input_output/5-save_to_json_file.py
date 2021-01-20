#!/usr/bin/python3
"""Creates a function to store JSON representation of object
to a file"""
import json


def save_to_json_file(my_obj, filename):
    """Stores the JSON representation of an object to a file"""

    with open(filename, 'w') as f:
        a = f.write(json.dumps(my_obj))
    f.close
    return a
