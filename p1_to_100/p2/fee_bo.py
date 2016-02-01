#!/usr/bin/python


def fibo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


def even_fibo_elems(up_to):
    n = 1
    fibo_n = fibo(n)
    while fibo_n < up_to:
        if fibo_n % 2 == 0:
            yield fibo_n
        n += 1
        fibo_n = fibo(n)

