#!/usr/bin/python3
"""
This is the "print_square" module. Usage: print_square(size)
>>> print_square(1)
#
"""


def print_square(size):
    """
    Prints a square with the character "#"
    """
    error1 = "size must be an integer"
    error2 = "size must be >= 0"

    if type(size) != int or type(size) == float:
        raise TypeError(error1)

    if size < 0:
        raise ValueError(error2)

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
    print
