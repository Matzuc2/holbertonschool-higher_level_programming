#!/usr/bin/python3
def uniq_add(my_list=[]):
    number = 0
    new = list(set(my_list))
    for i in new:
        number += i
    return (number)
