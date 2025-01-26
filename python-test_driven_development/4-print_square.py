#!/usr/bin/python3
def print_square(size):
    if isinstance(size, bool):
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    for _ in range(size):
        print('#' * size)