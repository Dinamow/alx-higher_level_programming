#!/usr/bin/python3
"""this is func file"""
import json
"""this is module"""


def load_from_json_file(filename):
    """this is func"""
    with open(filename, 'r') as file:
        json_data = file.read()
        return json.loads(json_data)
