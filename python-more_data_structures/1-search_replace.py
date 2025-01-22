#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = list.copy(my_list)
    for i in new:
        if i == search:
            new[i] = replace
    return (new)
