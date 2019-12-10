#!/usr/bin/python3
def fizzbuzz():
    """ This function will print \"Fizz\" instead of the multiples of 3,
        \"Buzz\" instead of the multiples of 5 and \"FizzBuzz\" instead
        of the multpiples of both 3 and 5 """

    for i in range(1, 101):
        if (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz", end = " ")
        elif (i % 3 == 0):
            print("Fizz", end = " ")
        elif (i % 5 == 0):
            print("Buzz", end = " ")
        else:
            print(i, end = " ")
