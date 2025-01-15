#!/usr/bin/python3
import sys


def main():
    number = 0
    if __name__ == '__main__':
        for i in range(1, len(sys.argv)):
            number += int(sys.argv[i])
    if len(sys.argv) > 1:
        print("{}".format(number))


main()
