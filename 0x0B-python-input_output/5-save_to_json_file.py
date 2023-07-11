#!/usr/bin/python3
import json
""" this is func file"""


def save_to_json_file(my_obj, filename):
    """this is the func"""
    with open(filename, mode='w') as file:
        file.write(json.dumps(my_obj))
