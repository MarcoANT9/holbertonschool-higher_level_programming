#!/usr/bin/python3

"""This is a class to define a Rectangle."""


class Rectangle:

    """A Rectangle Class."""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width * 2) + (self.height * 2)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        i = 0
        rectangle = ""
        while i < self.height:
            j = 0
            while j < self.width:
                rectangle = rectangle + "#"
                j += 1
            rectangle = rectangle + '\n'
            i += 1
        rectangle = rectangle.strip('\n')
        return rectangle

    def __repr__(self):
        text = '{self.__class__.__name__}({self.width}, {self.height})'
        rep_return = text.format(self=self)
        return rep_return

    def __del__(self):
        print("Bye rectangle...")

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        """Validates values for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Validates values for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
