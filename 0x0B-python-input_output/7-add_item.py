#!/usr/bin/python3
"""A script that adds all arguments to a python list,
    and then save them to a file
"""
from sys import argv
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


a = []
if path.exists("add_item.json"):
    a = load_from_json_file("add_item.json")
a = a + argv[1:]
save_to_json_file(a, "add_item.json")
