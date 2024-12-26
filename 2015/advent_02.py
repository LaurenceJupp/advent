#!/usr/bin/env python3
''' https://adventofcode.com/2015/day/2 '''

import itertools
import math

INPUT = 'input_02.txt'

def get_input():
    ''' Generate tuples of dimensions as input '''
    with open(INPUT, 'r', encoding='utf-8') as input02:
        for line in input02:
            yield tuple(int(x) for x in line.strip().split('x'))

def main():
    ''' Calculate total paper and ribbon for parts 1 and 2 '''
    total_paper = 0
    total_ribbon = 0
    for box in get_input():
        areas = tuple(i * j for i, j in itertools.combinations(box, 2))
        total_paper += 2 * sum(areas) + min(areas)
        total_ribbon += 2 * (sum(box) - max(box)) + math.prod(box)
    print(f'Part 1: {total_paper}\nPart 2: {total_ribbon}')

main()
