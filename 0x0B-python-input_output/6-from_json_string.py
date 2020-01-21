#!/usr/bin/python3
"""
This module returns the object(Python) representation of a json string.
"""


import json


def from_json_string(my_str):
    """
    This function takes a json (string) and converts it into its
    object (Python) representation. It returns the result.
    """

    return(json.loads(my_str))

if __name__ == "__main__":
    main()
