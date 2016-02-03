#!/usr/bin/python
import sys


def is_palyndrome(n):
    n_str = str(n)
    for i in xrange(len(n_str) / 2):
        if not n_str[i] == n_str[-(i + 1)]:
            return False
    return True


def max_to_min_sum_addends(target_sum, max_addend, min_addend):
    if target_sum - min_addend > max_addend:
        a = max_addend
        b = target_sum - max_addend
    else:
        a = target_sum - min_addend
        b = min_addend
    while not b > a:
        yield a, b
        a -= 1
        b += 1


def max_and_min_addend(digits):
    max_str = ""
    min_number = 0.1
    for i in xrange(digits):
        max_str += "9"
        min_number *= 10
    return int(max_str), int(min_number)


def find_biggest_palin(digits):
    max_number, min_number = max_and_min_addend(digits)
    for target_sum in reversed(xrange(min_number * 2, max_number * 2)):
        for a, b in max_to_min_sum_addends(target_sum, max_number, min_number):
            if is_palyndrome(a * b):
                return a * b


if __name__ == "__main__":
    print find_biggest_palin(int(sys.argv[1]))
