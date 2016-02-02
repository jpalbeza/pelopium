#!/usr/bin/python

import sys
from math import sqrt


def next_probable_prime(mul, non_mul_primes, next_mul):
    result = 0
    i = 1
    while result < next_mul:
        for additive in [1] + non_mul_primes:
            result = (mul * i) + additive
            if result < next_mul:
                yield result
            else:
                break
        i += 1


def starting_at_value(fake_prime_factors, prime_value):
    i = 0
    while fake_prime_factors[i] != prime_value:
        i += 1
    return fake_prime_factors[i:]

def find_primes_up_to(limit):
    found_primes = [2, 3, 5]
    mul_index = 1
    mul = 1
    for i in found_primes[0:mul_index]:
        mul *= i

    next_candidate = 0
    next_fake_prime_factors = found_primes
    while next_candidate < limit:
        mul *= found_primes[mul_index]
        mul_index += 1
        next_mul = mul * found_primes[mul_index]
        fake_prime_factors = starting_at_value(next_fake_prime_factors, found_primes[mul_index])
        next_fake_prime_factors = fake_prime_factors[0:]

        for candidate in next_probable_prime(mul, fake_prime_factors, next_mul):
            next_candidate = candidate
            next_fake_prime_factors.append(next_candidate)
            if next_candidate >= limit:
                break
            non_mul_limit = int(sqrt(next_candidate))
            is_prime = True
            for possible_mul in found_primes:
                if possible_mul <= non_mul_limit:
                    if next_candidate % possible_mul == 0:
                        is_prime = False
                else:
                    break
            if is_prime:
                found_primes.append(next_candidate)

    return found_primes


def find_biggest_prime_factor_of(n):
    limit = sqrt(n)
    for i in find_primes_up_to(limit)[::-1]:
        if n % i == 0:
            print i
            break


def main():
    n = int(sys.argv[1])
    find_biggest_prime_factor_of(n)

if __name__ == "__main__":
    main()

