#!/usr/bin/python3
"""
This is class, "Geometry" is not emtpy anymore, although it's
not that useful.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class only has one method."""

    def __init__(self, size):
        """ Initializes the class."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
