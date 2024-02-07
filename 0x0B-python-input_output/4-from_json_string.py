#!/usr/bin/python3
""" A function that returns an object (Python data structure)
    represented by a JSON string
"""
from json import loads as ld


def from_json_string(my_str):
    """ A function that returns an object (py data struct) ...."""
    return ld(my_str)
