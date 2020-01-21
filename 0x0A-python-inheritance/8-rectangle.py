#!/usr/bin/python3
"""
This is class, "Geometry" is not emtpy anymore, although it's
not that useful.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class only has one method."""

    def __init__(self, width, height):
        """ Initializes the class."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
