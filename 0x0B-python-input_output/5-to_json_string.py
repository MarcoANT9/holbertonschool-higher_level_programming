#!/usr/bin/python3
"""
This module returns the json representation of a string object.
"""


import json


def to_json_string(my_obj):
    """
    This function takes an object (string) and converts it in its
    json representation. It returns the result.
    """

    return(json.dumps(my_obj))



if __name__ == "__main__":
    main()
