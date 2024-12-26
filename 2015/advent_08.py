#!/usr/bin/env python3
''' https://adventofcode.com/2015/day/8 '''

import sys
from ast import literal_eval

INPUT = __file__.replace('advent_', 'input_').replace('py', 'txt')

def get_input():
    ''' Read puzzle input '''
    with open(INPUT, 'r', encoding='utf-8') as file:
        for line in file:
            yield line

def escape(line):
    ''' Add appropriate escape characters to line '''
    new = ''
    for char in line:
        if char in '"\\':
            new += f'\\{char}'
        else:
            new += char
    return f'"{new}"'

def main():
    ''' main '''
    part1 = 0
    part2 = 0

    for line in get_input():
        line = line.strip()
        part1 += len(line) - len(literal_eval(line))
        part2 += len(escape(line)) - len(line)

    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
