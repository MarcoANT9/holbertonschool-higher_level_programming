#!/usr/bin/python3
"""
This module writes an Object to a text file using a JSON
representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    This program takes <my_obj>, converts it into json format and
    writes it in <filename> file.
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        json.dump(my_obj, my_file)

if __name__ == "__main__":
    main()
