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
