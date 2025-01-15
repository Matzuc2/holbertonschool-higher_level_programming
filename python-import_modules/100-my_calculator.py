#!/usr/bin/python3
import sys
from calculator_1 import mul, add, sub, div


def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return (1)
    if (
        sys.argv[2] != "*"
        and sys.argv[2] != "+"
        and sys.argv[2] != "-"
        and sys.argv[2] != "/"
    ):
        print("Unknown operator. Available operators: +, -, * and /")
        return (1)

    if sys.argv[2] == "*":
        print(mul(int(sys.argv[1]), int(sys.argv[3])))
    elif sys.argv[2] == "+":
        print(add(int(sys.argv[1]), int(sys.argv[3])))
    elif sys.argv[2] == "-":
        print(sub(int(sys.argv[1]), int(sys.argv[3])))
    elif sys.argv[2] == "/":
        print(div(int(sys.argv[1]), int(sys.argv[3])))


if __name__ == "__main__":
    main()
