#!/usr/bin/env python3
''' https://adventofcode.com/####/day/# '''

import sys
import os
import time

INPUT = __file__.replace('advent_', 'input_').replace('py', 'txt')
MOVES = {'>' : complex(1, 0), '^' : complex(0, 1), '<' : complex(-1, 0), 'v' : complex(0, -1)}

def get_input():
    ''' Read puzzle input '''
    with open(INPUT, 'r', encoding='utf-8') as file:
        for line in file:
            pass
def print_puzzle(positions, puzzle):
    ''' Display puzzle map '''
    columns, rows = os.get_terminal_size()
    ymax = min(sum(1 for p in positions if p.real == 0), rows - 1)
    xmax = min(sum(1 for p in positions if p.imag == 0), columns - 1)

    display = '\033[F' * ymax
    for y in range(ymax):
        display += ''.join(('#' if puzzle[complex(x, y)] else '.') for x in range(xmax)) + '\n'
    sys.stdout.write(display)
    sys.stdout.flush()
    time.sleep(0.1)

def main():
    ''' main '''
    print(f'Part 1: {get_input()}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
