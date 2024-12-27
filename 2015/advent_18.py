#!/usr/bin/env python3
''' https://adventofcode.com/2015/day/18 '''

import sys
import os   # For animation
import time # For animation
from collections import defaultdict

INPUT = __file__.replace('advent_', 'input_').replace('py', 'txt')
NEIGHBOURS = (complex(1, 0), complex(0, 1), complex(-1, 0), complex(0, -1),
              complex(1, 1), complex(-1, 1), complex(-1, -1), complex(1, -1))

def get_input():
    ''' Read puzzle input '''
    lights = defaultdict(int)
    positions = []
    with open(INPUT, 'r', encoding='utf-8') as file:
        for y, line in enumerate(file):
            for x, char in enumerate(line.strip()):
                p = complex(x, y)
                positions.append(p)
                if char == '#':
                    lights[p] = 1

    return positions, lights

def print_map(positions, lights):
    ''' Display map of lights '''
    columns, rows = os.get_terminal_size()
    ymax = min(sum(1 for p in positions if p.real == 0), rows - 1)
    xmax = min(sum(1 for p in positions if p.imag == 0), columns - 1)
    display = '\033[F' * ymax
    for y in range(ymax):
        display += ''.join(('#' if lights[complex(x, y)] else '.') for x in range(xmax)) + '\n'
    sys.stdout.write(display)
    sys.stdout.flush()
    time.sleep(0.1)

def lights_stuck_on(positions, lights):
    ''' Some lights are stuck on '''
    ymax = sum(1 for p in positions if p.real == 0) - 1
    xmax = sum(1 for p in positions if p.imag == 0) - 1
    lights[complex(0, 0)] = 1
    lights[complex(0, ymax)] = 1
    lights[complex(xmax, 0)] = 1
    lights[complex(xmax, ymax)] = 1

def iteration(positions, lights):
    ''' An iteration of game of life '''
    new_lights = defaultdict(int)
    for p in positions:
        neighbours = sum(lights[p + q] for q in NEIGHBOURS)
        if lights[p]:
            if neighbours in (2, 3):
                new_lights[p] = 1
        else:
            if neighbours == 3:
                new_lights[p] = 1
    return new_lights

def main():
    ''' main '''
    # Part 1
    positions, lights = get_input()
    print_map(positions, lights)
    for _ in range(100):
        lights = iteration(positions, lights)
        print_map(positions, lights)
    part1 = sum(lights.values())

    # Part 2
    positions, lights = get_input()
    lights_stuck_on(positions, lights)
    print_map(positions, lights)
    for _ in range(100):
        lights = iteration(positions, lights)
        lights_stuck_on(positions, lights)
        print_map(positions, lights)
    part2 = sum(lights.values())

    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')

    return 0

if __name__ == '__main__':
    sys.exit(main())
