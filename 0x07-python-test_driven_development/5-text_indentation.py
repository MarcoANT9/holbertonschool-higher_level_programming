#!/usr/bin/python3
"""
This is the "text_indentation" module. Usage: text_indentation(text)
>>> text_indentation("Something here? I think not)
Something here? \n\n I think not
"""


def text_indentation(text):
    """
    Prints two new lines each time it finds "?", "." and ":"
    """
    error1 = "text must be a string"

    check = ["?", ".", ":"]

    if type(text) != str:
        raise TypeError(error1)

    i = 0
    while i < len(text):
        if text[i] in check:
            print(text[i])
            i += 1
            print()
        else:
            print(text[i], end="")
        i += 1
    print()
