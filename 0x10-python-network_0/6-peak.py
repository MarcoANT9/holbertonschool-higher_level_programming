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
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    middle_index = len(list_of_integers) // 2
    middle_value = list_of_integers[middle_index]

    left_value = find_peak(list_of_integers[:middle_index])
    right_value = find_peak(list_of_integers[middle_index:])

    if left_value > right_value:
        maxim = left_value
    else:
        maxim = right_value

    if middle_value > maxim:
        return middle_value
    else:
        return maxim
