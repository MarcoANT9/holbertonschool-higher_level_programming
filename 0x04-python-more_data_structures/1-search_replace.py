#!/usr/bin/python3
def search_replace(my_list, search, replace):

    '''This program searches and replaces all ocurrences of a "search"
       element and replaces them with "replace" value. It returns a new
       matrix containing the replaced elements.                     '''

    new_list = []
    for index in my_list:
        if index == search:
            new_list.append(replace)
        else:
            new_list.append(index)

    return new_list
