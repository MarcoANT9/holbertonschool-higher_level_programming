#!/usr/bin/python3

"""This class defines a Square with a size"""


class Square():
    """ A Square Class, has a private instance attribute: Size."""

    def __init__(self, size=0, position=(0, 0)):
        """Size definition."""
        self.size = size
        self.position = position

    def area(self):
        """The area of the square."""
        return self.__size ** 2

    def my_print(self):
        """The number of positions to translate the square."""
        for y in range(0, self.__position[1]):
            print()
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """Validates values for size"""
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
