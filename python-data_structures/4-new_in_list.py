#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)
    if idx > len(my_list):
        return (my_list)
    new_list = list.copy(my_list)
    for i in range(len(new_list)):
        if i == idx:
            new_list[i] = element
            return (new_list)
