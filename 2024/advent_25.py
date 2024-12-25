#!/usr/bin/env python3
''' https://adventofcode.com/2024/day/25 '''

INPUT = 'input_25.txt'

def get_input():
    ''' Return items as hex numbers '''
    with open(INPUT, 'r', encoding='utf-8') as input25:
        while item := input25.read(43).split():
            value = 0
            for y in range(7):
                for x in range(5):
                    if item[y][x] == '#':
                        value += (1 << y) << (x * 7)
            yield value


def main():
    ''' Read in locks and keys then add and check sums for digit overflows '''
    all_items = set(get_input())
    total = 0
    for item in all_items:
        for other in all_items:
            if not item & other:
                total += 1
    print(f'Part 1: {total//2}')

main()
