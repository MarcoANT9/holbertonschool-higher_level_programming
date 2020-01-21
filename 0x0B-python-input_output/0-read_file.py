#!/usr/bin/python3
"""
This module opens a file, reads and prints
each line into the stdout.
"""


def read_file(filename=""):
    """
    This function takes a file and opens it to read its contents.

    """
    with open("my_file_0.txt", "r", encoding="utf-8") as myfile:
        for myLine in myfile:
            print(myLine, end="")


if __name__ == "__main__":
    main()
