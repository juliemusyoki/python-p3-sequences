#!/usr/bin/env python3
def print_fibonacci(length):
    my_list = []
    a, b = 0, 1

    for _ in range(length):
        my_list.append(a)
        a, b = b, a + b

    print(my_list)
    