#!/usr/bin/python3
for tens_ in range(8):
    for units_ in range(tens_ + 1, 10):
        print("{:d}{:d}".format(tens_, units_), end=", ")
print("{:d}{:d}".format(8, 9))
