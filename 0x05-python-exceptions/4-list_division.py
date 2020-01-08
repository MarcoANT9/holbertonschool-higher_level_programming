#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    index = 0
    quot_list = []
    while index < list_length:

        try:
            quot = my_list_1[index] / my_list_2[index]

        except ZeroDivisionError:
            quot = 0
            print("division by 0")

        except (ValueError, TypeError):
            quot = 0
            print("wrong type")

        except IndexError:
            quot = 0
            print("out of range")

        finally:
            quot_list.append(quot)
            index += 1

    return quot_list

if __name__ == "__main__":
    main()
