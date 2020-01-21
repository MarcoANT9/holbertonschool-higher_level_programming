#!/usr/bin/python3
"""
This module converts a class into a json string.
"""


import json


def class_to_json(obj):
    """
    This function takes an object (class in this case) and returns
    the dictionary description with simple data struncture.
    """
    return (json.dumps(obj, default=lambda x: x.__dict__))

if __name__ == "__main__":
    main()
