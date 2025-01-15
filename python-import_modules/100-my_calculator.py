#!/usr/bin/python3
import sys
from calculator_1 import mul, add, sub, div


def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if (
        sys.argv[2] != '*'
        and sys.argv[2] != '+'
        and sys.argv[2] != '-'
        and sys.argv[2] != '/'
    ):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if sys.argv[2] == '*':
        result = mul(int(sys.argv[1]), int(sys.argv[3]))
        print(f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {result}")
    elif sys.argv[2] == '+':
        result = add(int(sys.argv[1]), int(sys.argv[3]))
        print(f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {result}")
    elif sys.argv[2] == '-':
        result = sub(int(sys.argv[1]), int(sys.argv[3]))
        print(f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {result}")
    elif sys.argv[2] == '/':
        result = div(int(sys.argv[1]), int(sys.argv[3]))
        print(f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {result}")


if __name__ == '__main__':
    main()
