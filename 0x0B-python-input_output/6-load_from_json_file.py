#!/usr/bin/python3
"""Creates a function that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file"""

    jstr = ""
    with open(filename, 'r') as f:
        for line in f:
            jstr += line
    obj = json.loads(jstr)
    f.closed
    return obj
