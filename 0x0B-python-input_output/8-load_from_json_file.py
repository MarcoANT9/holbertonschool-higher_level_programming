#!/usr/bin/python3
"""
This module creates an Object from a JSON string in a file.
"""


import json


def load_from_json_file(filename):
    """
    This function takes the json string from a file and creates the
    Python object.
    """
    with open(filename, encoding="utf-8") as myFile:
        obj = json.loads(myFile.read())
    return obj

if __name__ == "__main__":
    main()
