#!/usr/bin/python3
def remove_char_at(str, n):
    """ This Function will remove a char in a string at a given position """

    str_copy = str[:n] + str[n+1:]

    return str_copy
