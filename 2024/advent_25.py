#!/usr/bin/env python3
''' https://adventofcode.com/2024/day/25 '''

INPUT = 'input_25.txt'

def get_input():
    ''' Return keys and locks as hex numbers, distinguished by sign '''
    with open(INPUT, 'r', encoding='utf-8') as input25:
        while item := input25.read(43).split():
            value = 0
            for y in range(6):
                for x in range(5):
                    x_power = 16 ** x
                    trans = f'{item[y][4-x]}{item[y+1][4-x]}'
                    if trans == '#.':
                        # lock
                        value += y * x_power
                    elif trans == '.#':
                        # key
                        value -= (5-y) * x_power
            yield value


def main():
    ''' Read in locks and keys then add and check sums for digit overflows '''
    all_items = tuple(get_input())
    keys = set(-x for x in all_items if x < 0)
    locks = set(x for x in all_items if x > 0)

    total = 0
    for key in keys:
        for lock in locks:
            if int(max(hex(key + lock)[2:]), 16) < 6:
                total += 1
    print(f'Part 1: {total}')

main()
