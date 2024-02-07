#!/usr/bin/python3
"""
    A function that returns the dictionary description
    with simple data structure (list, dictionary, etc )
"""


def class_to_json(obj):
    return obj.__dict__
