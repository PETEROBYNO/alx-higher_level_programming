#!/usr/bin/python3

for alpha in range(97, 123):
    if chr(alpha) in "qe":
        continue
    print("{}".format(chr(alpha)), end="")
