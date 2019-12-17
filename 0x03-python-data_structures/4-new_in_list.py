#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    '''This function creates a new list with the elements of
       my_list list except for the one specified by the index
       position.                                          '''

    new_list = []
    if idx >= 0 and idx < len(my_list):
        for i in range(0, len(my_list)):
            if i == idx:
                new_list.append(element)
            else:
                new_list.append(my_list[i])

        return new_list

    return None
