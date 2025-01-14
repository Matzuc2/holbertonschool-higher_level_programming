#!/usr/bin/env python3
def print_last_digit(number):
    if number > 0:
        result = number % 10
        print(result, end="")
    else:
        result = number % -10
        result = result * (-1)
        print(result, end="")
    return (result)
