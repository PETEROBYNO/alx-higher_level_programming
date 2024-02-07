#!/usr/bin/python3
"""a function that appends a string at the end of a text file (UTF8)"""


def append_write(filename="", text=""):
    """A function that appends a string at the end of a text file"""
    with open(filename, 'a') as f:
        return f.write(text)
