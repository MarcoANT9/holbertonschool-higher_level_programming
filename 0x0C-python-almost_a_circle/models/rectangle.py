#!/usr/bin/python3
""" This class is a child class which inherits from "base"."""


from models.base import Base


class Rectangle(Base):
    """ This class defines a rectangle, inherits id from its parent class. """

    """====================================================================="""
    """= INIT & CLASS VARIABLES ============================================"""
    """====================================================================="""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ This function is the constructor of the class. """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """====================================================================="""
    """= METHODS ==========================================================="""
    """====================================================================="""

    def area(self):
        """ Public method, it returns the area of the Rectangle. """
        return (self.width * self.height)

    def display(self):
        """ Public method, it creates a representation of the Rectangle
            in the Standard Output.                                 """
        for k in range(0, self.y):
            print()
        for i in range(0, self.height):
            for h in range(0, self.x):
                print(" ", end="")
            for j in range(0, self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ Puclic method, makes a summary of the figure.                   """
        if self.width == 0 or self.height == 0:
            return ""
        name = self.__class__.__name__
        if name == "Rectangle":
            text = ("[{}] ({}) {}/{} - {}/{}".format(name, self.id, self.x,
                                                     self.y, self.width,
                                                     self.height))
        else:
            text = ("[{}] ({}) {}/{} - {}".format(name, self.id, self.x,
                                                  self.y, self.width))
        return text

    def to_dictionary(self):
        """ Returns a dictionary representation of the class """
        dictt = ({'id': self.id, 'x': self.x, 'y': self.y})
        dictt.update({'width': self.width})
        dictt.update({'height': self.height})
        return dictt

    def update(self, *args, **kwargs):
        """ Updates the Figure via arguments.                               """
        if len(args) != 0:
            if len(args) >= 6:
                raise OSError("Too much arguments")
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) == 5:
                self.y = args[4]
        else:
            self.id = kwargs.get('id', self.id)
            self.width = kwargs.get('width', self.width)
            self.height = kwargs.get('height', self.height)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    """====================================================================="""
    """= GETTERS & SETTERS ================================================="""
    """====================================================================="""

    @property
    def width(self):
        """ Property width, private. """
        return self.__width

    @width.setter
    def width(self, value):
        """ This setter assings value to width. """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Property height, private. """
        return self.__height

    @height.setter
    def height(self, value):
        """ This setter assings value to height. """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Property Position X, private. """
        return self.__x

    @x.setter
    def x(self, value):
        """ This setter, assings value to the x position. """
        if type(value) !=  int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Property Position Y, private. """
        return self.__y

    @y.setter
    def y(self, value):
        """ This setter, assings value to the y position. """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be greather or equal to 0")
        self.__y = value
