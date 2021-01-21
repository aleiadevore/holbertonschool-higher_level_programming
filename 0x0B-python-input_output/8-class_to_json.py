#!/usr/bin/python3
"""Creates a function to return dictionary description for
JSON serialization of an object"""
import json


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    serialization of an object"""

    s = json.dumps(obj.__dict__)
    return json.loads(s)
