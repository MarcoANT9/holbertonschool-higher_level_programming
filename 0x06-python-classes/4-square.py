#!/usr/bin/python3

"""This class defines a Square with a size"""


class Square:
    """ A Square Class, has a private instance attribute: Size."""

    def __init___(self, size=0):
        """ Size definition. """
        self.size = size

    def area(self):
        """The area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """The area of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Validates values for size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
