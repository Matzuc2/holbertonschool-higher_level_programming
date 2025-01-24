#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        new = a / b
    except ZeroDivisionError:
        new = None
        return None
    finally:
        print("Inside result: {}".format(new))
        return new
