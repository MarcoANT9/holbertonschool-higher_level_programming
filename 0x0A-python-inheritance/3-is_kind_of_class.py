#!/usr/bin/python3
"""
This module tests if an object is an instance
of a class of an instance of a subclass of the
first class.
"""


def is_kind_of_class(obj, a_class):
    """ The object must be an instance of the class or
        the type of the object must be a subclass of the
        first one."""

    if isinstance(obj, a_class) or issubclass(a_class, type(obj)):
        return True
    return False

if __name__ == "__main__":
    main()
