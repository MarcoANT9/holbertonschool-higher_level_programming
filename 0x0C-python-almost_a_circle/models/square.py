#!/usr/bin/python3
""" This class is a child class which inherits from "Rectangle",
    which is already a child class of "Base"."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ This class defines a square, inherits id from its parent class. """

    """====================================================================="""
    """= INIT & CLASS VARIABLES ============================================"""
    """====================================================================="""

    def __init__(self, size, x=0, y=0, id=None):
        """ This function is the constructor of the class. """
        super().__init__(size, size, x, y, id)

    """====================================================================="""
    """= METHODS ==========================================================="""
    """====================================================================="""

    def update(self, *args, **kwargs):
        """ Updates the values in the class """
        if len(args) != 0:
            if len(args) >= 5:
                raise OSError("Too much arguments")
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) == 4:
                self.y = args[3]
        else:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        """ Returns a dictionary representation of the class """
        dictt = ({'id': self.id, 'x': self.x, 'y': self.y})
        dictt.update({'size': self.size})
        return dictt

    """====================================================================="""
    """= GETTERS & SETTERS ================================================="""
    """====================================================================="""

    @property
    def size(self):
        """ Getter for the size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for the size """
        self.width = value
        self.height = value
