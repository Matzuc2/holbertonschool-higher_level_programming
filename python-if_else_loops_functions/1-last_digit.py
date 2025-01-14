#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    number2 = number % 10
if number == 0:
    number2 = 0
if number < 0:
    number2 = number % -10
if number2 > 5:
    print("Last digit of {} is {} ".format(number, number2), end="")
    print("and is greater than 5")
elif number2 < 6 and number2 != 0:
    print("Last digit of {} is {} ".format(number, number2), end="")
    print("and is less than 6 and not 0")
elif number2 == 0:
    print("Last digit of {} is {} and is 0".format(number, number2))
