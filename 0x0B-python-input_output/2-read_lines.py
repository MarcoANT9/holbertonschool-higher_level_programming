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
        if nb_lines <= 0 and nb_lines > len(list(myfile)):
            for lines in myfile:
                print(lines, end="")

        else:
            for i in range(0, nb_lines):
                print(myfile.readline())


if __name__ == "__main__":
    main()
