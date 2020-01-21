#!/usr/bin/python3
"""
This module opens a file, reads and counts
each line to return the number of readed lines.
"""


def number_of_lines(filename=""):
    """
    This function takes a file and opens it to count its lines.

    """
    with open(filename, "r", encoding="utf-8") as myfile:
        number_lines = 0
        for myLine in myfile:
            number_lines += 1

    return number_lines

if __name__ == "__main__":
    main()
