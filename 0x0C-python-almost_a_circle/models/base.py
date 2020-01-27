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
    def create(cls, **dictionary):
        """ This static method returns an instance with all attributes set """
        if cls.__name__ == "Rectangle":
            new_class = cls(1, 2)
        else:
            new_class = cls(1)
        new_class.update(**dictonary)
        return new_class

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as myfile:
                text = Base.from_json_string(myfile.readline())
                lista = []
                for i in text:
                    lista.append(cls.create(**i))
                return lista

        except:
            return []

    @staticmethod
    def from_json_string(json_string):
        """ Takes a json string and transform it into its python equivalent """
        if json_string is None or len(json_string) == 0:
            return ([])
        return (json.loads(json_string))

    @staticmethod
    def to_json_string(list_dictionaries):
        """ This static method creates a json string from a dictionary """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
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
