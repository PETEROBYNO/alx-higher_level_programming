#!/usr/bin/python3
"""Defines a class LockedClass"""


class LockedClass:
    """
    Function that prevents the user from dynamically
    creating new instance attributes...
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """Creates new instance of Licked Class."""

        self.first_name = "first_name"
