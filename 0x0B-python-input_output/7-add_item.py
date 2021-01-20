#!/usr/bin/python3
"""Adds all items to a python list and saves to file"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


items = sys.argv
items.pop(0)
try:
    with open("add_item.json", 'x') as f:
        save_to_json_file(items, "add_item.json")
except:
    newlist = load_from_json_file("add_item.json")
    save_to_json_file(newlist + items, "add_item.json")
