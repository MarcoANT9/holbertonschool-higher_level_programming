#!/usr/bin/python3
"""
This is the "add_integer" module. Usage: add_integer(a, b)
>>> add_integer(2, 3)
5
"""

def add_integer(a, b = 98):
    """
    Returns the sum of two integers.
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("./test/0-add_integer.txt")
