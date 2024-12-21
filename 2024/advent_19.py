#!/usr/bin/env python3
''' Advent of Code 2024 Day 19 '''
from functools import cache
from itertools import repeat
from concurrent.futures import ProcessPoolExecutor

INPUT = 'input_19.txt'

def get_input():
    ''' Parse input file and return tuples of towels and patterns '''
    with open(INPUT, 'r', encoding='utf-8') as input19:
        towels = tuple(x.strip() for x in input19.readline().split(','))
        patterns = tuple(x for x in input19.read().split())
    return towels, patterns

@cache
def count(pat, towels):
    ''' Number of ways of generating pattern 'pat' with towels '''
    return sum(count(pat[len(t):], towels) for t in towels if pat.startswith(t)) if pat else 1

def main():
    ''' Run count() on each pattern and report count of non-zeros, and the sum '''
    towels, patterns = get_input()
    with ProcessPoolExecutor(max_workers=8) as executor:
        counts = tuple(executor.map(count, patterns, repeat(towels), chunksize=len(patterns)//8+1))
    print(f'Part 1: {sum(1 for x in counts if x)}\nPart 2: {sum(counts)}')

main()
