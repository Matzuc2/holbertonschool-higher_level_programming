#!/usr/bin/python3
import sys
from calculator_1 import mul, add, sub, div


def main():
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if (
        operator != '*'
        and operator != '+'
        and operator != '-'
        and operator != '/'
    ):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if operator == '*':
        result = mul(a, b)
        print(f"{a} {operator} {b} = {result}")
    elif operator == '+':
        result = add(a, b)
        print(f"{a} {operator} {b} = {result}")
    elif operator == '-':
        result = sub(a, b)
        print(f"{a} {operator} {b} = {result}")
    elif operator == '/':
        result = div(a, b)
        print(f"{a} {operator} {b} = {result}")


if __name__ == "__main__":
    main()
