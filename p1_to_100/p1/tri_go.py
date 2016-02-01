#!/usr/bin/python


def multiples_of(step, up_to, starts_with=0, except_multiple_of = None):
    num = starts_with
    while num < up_to:
        if except_multiple_of and not (num % except_multiple_of) > 0:
            pass
        else:
            yield num
        num += step


def sum_mul_of_3_or_5():
    return sum(multiples_of(3, 1000, except_multiple_of=5)) + sum(multiples_of(5, 1000))


print sum_mul_of_3_or_5()
