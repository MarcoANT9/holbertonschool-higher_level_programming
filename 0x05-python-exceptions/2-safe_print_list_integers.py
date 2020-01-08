#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    index = 0
    numbers_printed = 0

    while (index < x):
        try:
            print("{:d}".format(my_list[index]), end="")

        except (ValueError, TypeError):
            index += 1

        except IndexError:
            raise
            return numbers_printed

        else:
            numbers_printed += 1
            index += 1

    print("")
    return numbers_printed
if __name__ == "__main__":
    main()
