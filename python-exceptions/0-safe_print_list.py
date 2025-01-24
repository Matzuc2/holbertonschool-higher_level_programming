#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    numb = 0
    for i in range(0, x):
        try:
            print(my_list[i], end="")
            numb += 1
        except IndexError:
            pass
    print()
    return (numb)
