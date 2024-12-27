#!/usr/bin/env python3
''' https://adventofcode.com/2015/day/13 '''

import sys
from collections import defaultdict
from itertools import permutations, pairwise

INPUT = __file__.replace('advent_', 'input_').replace('py', 'txt')

def get_input():
    ''' Return puzzle input as set of people and dict of happiness changes by pairs '''
    people = set()
    happiness = defaultdict(int)
    with open(INPUT, 'r', encoding='utf-8') as file:
        for line in file:
            # Sneak in a minus sign for 'lose'
            word = line.replace('lose ', 'gain -').split()

            people.add(word[0])

            # Combine pair of names in alphabetical order
            pair = ','.join(sorted((word[0], word[-1][:-1])))
            happiness[pair] += int(word[3])
    return people, happiness

def happiest(people, happiness):
    ''' Calculate maximum happiness from arranging people - the ends wrap '''
    return max(sum(happiness[','.join(sorted(x))] for x in pairwise(arrange + (arrange[0],)))
               for arrange in permutations(people))

def main():
    ''' main '''
    people, happiness = get_input()
    print(f'Part 1: {happiest(people, happiness)}')
    print(f'Part 2: {happiest(people | {"me"}, happiness)}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
