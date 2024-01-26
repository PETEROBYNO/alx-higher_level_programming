#!/usr/bin/python3
'''
A simple print_square module
size is the size length of the square
size must be an integer, otherwise raise a TypeError

You are not allowed to import any module
'''


def print_square(size):
    ''' A function that prints a square with the character'''
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >=')

    for _ in range(size):
        print('#' * size)
