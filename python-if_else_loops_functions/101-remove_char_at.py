#!/usr/bin/python3
def remove_char_at(str, n):
    if str == None:
        return (None)
    str1 = ""
    if n != 0:
        str1 = str[0]
    else:
        str1 = str[1]
    for i in range(1, len(str)):
        if i == n:
            continue
        str1 += str[i]
    return (str1)
