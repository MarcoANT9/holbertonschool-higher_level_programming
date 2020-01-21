#!/usr/bin/python3
"""
This module converts a class into a json string.
"""



def class_to_json(obj):
    """
    This function takes an object (class in this case) and returns
    the dictionary description with simple data struncture.
    """
    return obj.__dict__

if __name__ == "__main__":
    main()
