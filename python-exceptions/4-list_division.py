#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for i in range(list_length):
        try:
            numb = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            numb = 0
        except TypeError:
            print("wrong type")
            numb = 0
        except ZeroDivisionError:
            print("division by 0")
            numb = 0
        finally:
            new.append(numb)
    return (new)
