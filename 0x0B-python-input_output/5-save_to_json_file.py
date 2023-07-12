#!/usr/bin/python3
"""this is func file"""
import json
""" this is module"""


def save_to_json_file(my_obj, filename):
    """this is the func"""
    with open(filename, mode='w') as file:
        return json.dump(my_obj, file, indent=4)
