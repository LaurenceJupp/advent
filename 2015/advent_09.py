#!/usr/bin/env python3
''' https://adventofcode.com/2015/day/9 '''

import sys
from itertools import permutations, pairwise

INPUT = __file__.replace('advent_', 'input_').replace('py', 'txt')

def get_input():
    ''' Read puzzle input '''
    places = set()
    distances = {}
    with open(INPUT, 'r', encoding='utf-8') as file:
        for line in file:
            remainder, distance = line.split(' = ')
            place1, place2 = remainder.split(' to ')
            places |= {place1, place2}
            distances[tuple(sorted([place1, place2]))] = int(distance)
    return places, distances

def main():
    ''' main '''
    p, d = get_input()
    dist = [sum(d[tuple(sorted((x, y)))] for x, y in pairwise(r)) for r in permutations(p)]
    print(f'Part 1: {min(dist)}')
    print(f'Part 2: {max(dist)}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
