#!/usr/bin/python3
""" This is a class named Student."""


class Student():
    """ This class defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialices the class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        dicti = self.__dict__

        if attrs is not None and all(type(atr) == str for atr in attrs):
            return {atr: dicti[atr] for atr in dicti if atr in attrs}
        return dicti

    def reload_from_json(self, json):

        for key in json.keys():
            self.__dict__[key] = json[key]
