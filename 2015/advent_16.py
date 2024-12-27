#!/usr/bin/env python3
''' https://adventofcode.com/2015/day/16 '''

import sys

INPUT = __file__.replace('advent_', 'input_').replace('py', 'txt')
MFCSAM_STR = '''
children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1'''
MFCSAM = {k : int(v) for prop in MFCSAM_STR.strip().splitlines() for k, v in [prop.split(': ')]}

def get_input():
    ''' Yield puzzle input as dictionaries for each aunt '''
    with open(INPUT, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.split(': ', 1)[1]
            yield {k : int(v) for prop in line.split(', ') for k, v in [prop.split(': ')]}

def main():
    ''' main '''
    lots = max(MFCSAM.values()) + 1

    part1 = None
    part2 = None
    for sue, memory in enumerate(get_input(), 1):
        if part1 is None and MFCSAM | memory == MFCSAM:
            part1 = sue
        if (part2 is None and
            memory.pop('cats', lots) > MFCSAM['cats'] and
            memory.pop('trees', lots) > MFCSAM['trees'] and
            memory.pop('pomeranians', 0) < MFCSAM['pomeranians'] and
            memory.pop('goldfish', 0) < MFCSAM['goldfish'] and
            MFCSAM | memory == MFCSAM):
            part2 = sue

    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')

    return 0

if __name__ == '__main__':
    sys.exit(main())
