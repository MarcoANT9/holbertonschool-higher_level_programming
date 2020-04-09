#!/usr/bin/python3
""" This module will find the peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ This function will find the greater value on a list of integers
        Arguments:
            list_of_integers: A list containing the integers to get the peak.

        Return:
            The greates value in the list.
    """
    if list_of_integers == []:
        return None

    list_of_integers.sort()
    return list_of_integers[-1]
