#!/usr/bin/python3
""" A function that writes an Object to a text file,
    using a JSON representation
"""
from json import dumps as dp


def save_to_json_file(my_obj, filename):
    """ a function that writes an Object to a text file... """
    with open(filename, 'w') as f:
        a = dp(my_obj)
        f.write(a)
