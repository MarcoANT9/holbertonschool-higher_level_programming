#!/usr/bin/python3
"""
This is class, "Geometry" is not emtpy anymore, although it's
not that useful.
"""


class BaseGeometry():
    """This class only has one method."""

    def area(self):
        """ This was supposed to calculate the area of a figure...
            right now all it can do is raise an exception...   """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater that 0".format(name))
