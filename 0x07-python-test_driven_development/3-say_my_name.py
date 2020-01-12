#!/usr/bin/python3
"""
This is the "say_my_name" module. Usage: say_my_name(first_name, last_name="")
>>> say_my_name("Marco", "Antonio")
My name is Marco Antonio
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>
    """

    error1 = "first_name must be a string"
    error2 = "last_name must be a string"

    if type(first_name) != str:
        raise TypeError(error1)
    if type(last_name) != str:
        raise TypeError(error2)

    print("My name is {} {}".format(first_name, last_name))
