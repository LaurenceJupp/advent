#!/usr/bin/env python3
''' https://adventofcode.com/2015/day/17 '''

import sys
from functools import cache

INPUT = __file__.replace('advent_', 'input_').replace('py', 'txt')

def get_input():
    ''' Yield puzzle input as tuple of sizes '''
    with open(INPUT, 'r', encoding='utf-8') as file:
        return tuple(int(x) for x in file.read().split())

@cache
def fill(quantity, sizes, containers):
    for index, (size, container) in enumerate(zip(sizes, containers)):
        if size == quantity:
            yield (container,)
        elif size < quantity:
            # Remove container from lists
            new_sizes = list(sizes)
            new_containers = list(containers)
            new_sizes.pop(index)
            new_containers.pop(index)
            # Use the rest
            for others in fill(quantity - size, tuple(new_sizes), tuple(new_containers)):
                yield tuple(sorted([container] + list(others)))

def main():
    ''' main '''
    sizes = get_input()
    possibilities = set(fill(150, sizes, tuple(range(len(sizes)))))
    print(f'Part 1: {len(possibilities)}')

    minimum = min(len(x) for x in possibilities)
    part2 = sum(1 for x in possibilities if len(x) == minimum)
    print(f'Part 2: {part2}')

    return 0

if __name__ == '__main__':
    sys.exit(main())
