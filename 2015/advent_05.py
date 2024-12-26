#!/usr/bin/env python3
''' https://adventofcode.com/2015/day/5 '''

import sys
from collections import Counter
from string import ascii_lowercase

INPUT = __file__.replace('advent_', 'input_').replace('py', 'txt')

def get_input():
    ''' Read puzzle input '''
    with open(INPUT, 'r', encoding='utf-8') as file:
        for line in file:
            yield line

def main():
    ''' main '''
    part1 = 0
    part2 = 0
    for line in get_input():
        # Part 1
        c = Counter(line)
        if (sum(c[x] for x in 'aeiou') > 2 and
            any(x*2 in line for x in ascii_lowercase) and
            not any(x in line for x in ('ab', 'cd', 'pq', 'xy'))):
            part1 += 1

        # Part 2
        if (all(any(x) for x in zip(*((line.count(line[i:i + 2]) > 1, line[i] == line[i + 2])
                                      for i in range(len(line) - 2))))):
            part2 += 1
    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
