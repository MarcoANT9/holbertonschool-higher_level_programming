#!/usr/bin/python3
"""
This module opens a file, reads a defined number of
lines and print them into the stdout.
"""


def read_lines(filename="", nb_lines=0):
    """
    This function takes a file and opens it to print a determined
    number of lines.
    """
    with open(filename, mode="r", encoding="utf-8") as myfile:
        if nb_lines <= 0 or nb_lines >= sum(1 for lines in myfile):
            myfile.seek(0)
            print(myfile.read(), end="")

        else:
            myfile.seek(0)
            for i in range(0, nb_lines):
                print(myfile.readline(), end="")


if __name__ == "__main__":
    main()
