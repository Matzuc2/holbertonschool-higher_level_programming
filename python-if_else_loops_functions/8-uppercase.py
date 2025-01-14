#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97:
            print("{}".format(chr(ord(i)-32)), end="")
        elif ord(i) < 97:
            print("{}".format(i), end="")
    print()
