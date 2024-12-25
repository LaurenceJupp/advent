#!/usr/bin/env python3
''' https://adventofcode.com/2024/day/25 '''

INPUT = 'input_25.txt'

def get_input():
    ''' Return items as bitmasks '''
    with open(INPUT, 'r', encoding='utf-8') as input25:
        while item := input25.read(43).split():
            yield sum((1 << y) << (x * 7) for y in range(7) for x in range(5) if item[y][x] == '#')

def main():
    ''' Check for clashing bits '''
    all_items = set(get_input())
    total = sum(1 for x in all_items for y in all_items if not x & y)
    print(f'Part 1: {total//2}')

main()
