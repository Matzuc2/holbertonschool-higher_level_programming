#!/usr/bin/python3
def remove_char_at(str, n):
    if n == None:
        return (str)
    if n > len(str):
        return(str)
    if str == None or str == "":
        return (None)
    str1 = ""
    for i in range(len(str)):
        if i == n:
            continue
        str1 += str[i]
    return (str1)
