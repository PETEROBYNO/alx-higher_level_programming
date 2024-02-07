#!/usr/bin/python3
""" A function that returns the Json repr of an object"""
from json import dumps as dp


def to_json_string(my_obj):
    """A function that returns the Json repr of an object"""
    return dp(my_obj)
