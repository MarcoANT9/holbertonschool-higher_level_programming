#!/usr/bin/python3
def islower(c):
    """ This function will determine if a character is in lowercase """
    if ord(c) in range(97, 133):
        return True
    return False
