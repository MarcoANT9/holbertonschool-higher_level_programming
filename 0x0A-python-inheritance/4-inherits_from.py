#!/usr/bin/python3
"""
This module tests if an object is an instance
of a class that inherited from the specified class.
"""


def inherits_from(obj, a_class):
    """ The object must be an instance of a subclass."""

    if super(a_class, obj) and not type(obj) == a_class:
        return True
    return False

if __name__ == "__main__":
    main()
