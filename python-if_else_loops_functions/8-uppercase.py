#!/usr/bin/python3
def uppercase(str):
    for i in str:
        number = ord(i)-32
        if ord(i) >= 97:
            i = chr(number)
        print("{}".format(i), end="")
    print()
