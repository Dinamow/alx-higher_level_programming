#!/usr/bin/python3
import json
""" this is func file"""


def save_to_json_file(my_obj, filename):
    """this is the func"""
    with open(filename, mode='w') as file:
        json.dump(my_obj, file, indent=4)
