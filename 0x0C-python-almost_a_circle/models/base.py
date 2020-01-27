#!/usr/bin/python3
""" This class will be the "base" for all other classes in the project."""


import json


class Base():
    """ This class will be the foundation of the project, as all other classes
        will be derived from this one.                                     """

    """====================================================================="""
    """= INIT & CLASS VARIABLES ============================================"""
    """====================================================================="""

    __nb_objects = 0

    def __init__(self, id=None):
        """ This function is the constructor of the class. """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    """====================================================================="""
    """= METHODS ==========================================================="""
    """====================================================================="""

    @staticmethod
    def to_json_string(list_dictionaries):
        """ This static method creates a json string from a dictionary """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ([])
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ This class method saves a list of json into a file """
        filename = cls.__name__
        dictt = []
        if list_objs:
            for i in list_objs:
                dictt.append(cls.to_dictionary(i))

        with open(filename + ".json", "w") as myfile:
            myfile.write(cls.to_json_string(dictt))

    """====================================================================="""
    """= GETTERS AND SETTERS ==============================================="""
    """====================================================================="""
