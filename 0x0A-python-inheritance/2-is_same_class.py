#!/usr/bin/python3
"""
This module tests if an object is exactly an
instance of a class
"""


def is_same_class(obj, a_class):
    """ To be an exact instance of a class, the object
        must be an instance of a class and have the same
        type as the class."""

    if isinstance(obj, a_class) and type(obj) == a_class:
        return True
    return False

if __name__ == "__main__":
    main()
