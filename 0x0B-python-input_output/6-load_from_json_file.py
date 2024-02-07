#!/usr/bin/python3
"""A function that creates an object from a Json file"""
from json import loads as ld


def load_from_json_file(filename):
    """A function that creates an object from a json file"""
    with open(filename, 'r') as f:
        return ld(f.read())
