#!/usr/bin/env python3
''' https://adventofcode.com/2015/day/20 '''

from functools import cache

INPUT = 36000000
PRIME_LIMIT = INPUT // 10

def eratosthenes():
    ''' Primes up to PRIME_LIMIT '''
    is_prime = [True for i in range(PRIME_LIMIT + 1)]
    is_prime[0] = False
    is_prime[1] = False

    for p in range(2, int(PRIME_LIMIT**0.5 + 1)):
        if is_prime[p]:
            for i in range(p**2, PRIME_LIMIT + 1, p):
                is_prime[i] = False
    return tuple(is_prime)

IS_PRIME = eratosthenes()

@cache
def factors(n):
    ''' Factorize integer n '''
    if n < 2 or n <= PRIME_LIMIT and IS_PRIME[n]:
        return {n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            break
    others = factors(n // i)
    return set(x * i for x in others) | others | {i}

def main():
    ''' Factorize house number to determine presents '''

    part = [None, None]
    for i in range(1, INPUT):
        f = factors(i)
        if part[0] is None and 10 * sum(f) >= INPUT:
            part[0] = i

        if part[1] is None:
            limit = i // 50
            if 11 * sum(x for x in f if x >= limit) >= INPUT:
                part[1] = i

        if all(part):
            break

    print('\n'.join(f'Part{i}: {x}' for i, x in enumerate(part, 1)))
main()
