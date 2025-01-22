#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new2 = list(set(set_1) - set(set_2))
    new1 = list(set(set_2) - set(set_1))
    result = new1 + new2
    return (result)
