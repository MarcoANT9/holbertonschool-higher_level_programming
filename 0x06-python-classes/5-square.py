#!/usr/bin/python3

"""This class defines a Square with a size"""


class Square():
    """ A Square Class, has a private instance attribute: Size."""

    def __init__(self, size=0):
        """Size definition."""
        self.size = size

    def area(self):
        """The area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Custom print to the stdout a square composed of #."""
        if self.size == 0:
            print("")
        for i in range(0, self.size):
            for j in range(0, self.size):
                print("#", end="")
            print("")

    @property
    def size(self):
        """The area of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Validates values for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
