#!/usr/bin/python3
'''
A Simple addition module
'''


def add_integer(a, b=98):
    ''' a function that add two integers or floats. '''
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    result = int(a) + int(b)
    return result


if __name__ == '__main__':
    from doctest import testfile
    testfile('test/0-add_integer.txt')
