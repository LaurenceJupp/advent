#!/usr/bin/env python3
''' https://adventofcode.com/2015/day/3 '''

import sys

INPUT = __file__.replace('advent_', 'input_').replace('.py', '.txt')
MOVES = {'>' : complex(1, 0), '^' : complex(0, 1), '<' : complex(-1, 0), 'v' : complex(0, -1)}

def get_input():
    ''' Read puzzle input '''
    with open(INPUT, 'r', encoding='utf-8') as file:
        return file.read().strip()

def main():
    ''' main '''
    # Part 2 Santa, Part 2 Robosanta, Part1 Santa
    santa = [complex(0, 0)] * 3
    # Part 1, Part 2
    visited = [{santa[0]}, {santa[0]}]
    for i, m in enumerate(get_input()):
        # Part 1
        santa[2] += MOVES[m]
        visited[0].add(santa[2])
        # Part2
        santa[i & 1] += MOVES[m]
        visited[1] |= set(santa[:-1])
    print('\n'.join(f'Part {i}: {len(v)}' for i, v in enumerate(visited, 1)))
    return 0

if __name__ == '__main__':
    sys.exit(main())
