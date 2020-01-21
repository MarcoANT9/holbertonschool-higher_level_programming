#!/usr/bin/python3
"""
This module opens a file, writes a defined text in it
and returns the number of character writen.
"""


def append_write(filename="", text=""):
    """
    This function takes a file and opens it to write a determined
    sentence on it, if the file doesn't exists, it's created; if
    the file does exists, the text is appended.
    """
    with open(filename, mode="a", encoding="utf-8") as myfile:
        return(myfile.write(text))

if __name__ == "__main__":
    main()
