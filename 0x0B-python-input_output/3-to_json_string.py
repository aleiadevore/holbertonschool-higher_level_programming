#!/usr/bin/python3
"""Creates a function that returns a JSON representation
of an object"""
import json


def to_json_string(my_obj):
    """Returns a JSON representation of an object"""

    return json.dumps(my_obj)
