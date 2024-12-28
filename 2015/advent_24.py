#!/usr/bin/env python3
''' https://adventofcode.com/2015/day/24 '''

import sys
from functools import cache

INPUT = __file__.replace('advent_', 'input_').replace('py', 'txt')

length = 0

def get_input():
    ''' Read puzzle input '''
    with open(INPUT, 'r', encoding='utf-8') as file:
        for line in file:
            yield int(line)

@cache
def pack(target, items):
    global length

    if len(items) < length:
        return []

    if target < 0:
        return []

    if target == 0:
        if len(items) > length:
            length = len(items)
        return [items]

    ret = []
    for item in items:
        new_items = tuple(x for x in items if x != item)
        if result := pack(target - item, new_items):
            ret.extend(result)
    return ret

def minimum_entanglement(arrangements_other, items, minimum_length):
    min_entanglement = None
    for others in arrangements_other:
        if len(others) == minimum_length:
            entanglement = 1
            for x in items:
                if x not in others:
                    entanglement *= x
            if min_entanglement is None or entanglement < min_entanglement:
                min_entanglement = entanglement
    return min_entanglement

def main():
    ''' main '''
    global length
    items = tuple(sorted(list(get_input()), reverse=True))

    length = 0
    target = sum(items) // 3
    part1 = minimum_entanglement(set(pack(target, items)), items, length)
    print(f'Part 1: {part1}')

    length = 0
    target = sum(items) // 4
    part2 = minimum_entanglement(set(pack(target, items)), items, length)
    print(f'Part 2: {part2}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
