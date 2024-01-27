#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if 97 <= ord(c) <= 122:
            upper_char = chr(ord(c) - 32)
        else:
            upper_char = c
        print("{:s}".format(upper_char), end="")
    print()
