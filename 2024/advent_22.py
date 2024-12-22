#!/usr/bin/env python3
''' https://adventofcode.com/2024/day/22 '''
from collections import defaultdict
from itertools import repeat

INPUT = 'input_22.txt'

def get_input():
    ''' Input as list of integers '''
    with open(INPUT, 'r', encoding='utf-8') as input24:
        return (int(x) for x in input24.read().splitlines())

def iterate(old):
    ''' Derive next number in sequence '''
    old ^= (old << 6) & 0xffffff
    old ^= (old >> 5)
    old ^= (old << 11) & 0xffffff
    return old

def sequence_prices(secret, sequence_map):
    ''' Iterate secret number, storing price sequence info '''
    old = secret
    old_price = old % 10
    sequence = []
    done = set()
    for index in range(2000):
        new = iterate(old)
        new_price = new % 10
        sequence.append(new_price - old_price)
        seq = tuple(sequence[-4:])
        if len(seq) == 4 and not seq in done:
            sequence_map[seq] += new_price
            done.add(seq)
        old = new
        old_price = new_price
    return new

def main():
    ''' Accumulate sequence prices for each secret number '''
    sequence_map = defaultdict(int)
    total = sum(map(sequence_prices, get_input(), repeat(sequence_map)))
    print(f'Part 1: {total}')
    print(f'Part 2: {max(sequence_map.values())}')

main()
