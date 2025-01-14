#!/usr/bin/python3
for i in range(0, 99):
    if i < 10:
        print(0, end="")
    if i == 98:
        print("{}".format(i))
    else:
        print("{}, ".format(i), end="")
