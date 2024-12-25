#!/usr/bin/env python3
''' https://adventofcode.com/2024/day/25 '''

INPUT = 'input_25.txt'

def get_input():
    ''' Return items as bitmasks '''
    with open(INPUT, 'r', encoding='utf-8') as input25:
        while item := input25.read(43).replace('\n',''):
            yield sum(1 << i for i, x in enumerate(item) if x == '#')

def main():
    ''' Check for clashing bits '''
    all_items = set(get_input())
    double_count = sum(1 for x in all_items for y in all_items if not x & y)
    print(f'Part 1: {double_count//2}')

main()
