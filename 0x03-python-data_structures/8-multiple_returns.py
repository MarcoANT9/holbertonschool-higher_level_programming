#!/usr/bin/python3
def multiple_returns(sentence):

    '''This function takes a sentence and returns a tuple which
       contains the length of the string and its first character,
       should the string be empty, it will return None as first
       character.                                             '''

    if len(sentence) == 0:
        r_tuple = 0, None
        return r_tuple

    else:

        r_tuple = len(sentence), sentence[0]
        return r_tuple
