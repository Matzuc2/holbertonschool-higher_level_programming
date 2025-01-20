#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    string = ""
    for i in range(len(my_string)):
        if my_string[i] == "c" or my_string[i] == "C":
            string += my_string[i]
    return (string)
