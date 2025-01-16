import sys


def print_to_stdout(*a):

    # Here a is the array holding the objects
    # passed as the argument of the function
    print(*a, file=sys.stdout)


print_to_stdout("#pythoniscool")
