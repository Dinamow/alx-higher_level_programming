#!/usr/bin/python3
"""this file for func"""


def text_indentation(text):
    """
    text_indentation
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    text = text.replace('.', '.\n')
    text = text.replace('?', '?\n')
    text = text.replace(':', ':\n')
    text = text.split('\n')
    for x in range(len(text)):
        text[x] = text[x].strip()
    for x in range(len(text) - 1):
        text[x] = (text[x] + "\n\n")
    for x in text:
        print(x, end="")
