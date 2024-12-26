#!/usr/bin/env python3
''' https://adventofcode.com/2015/day/6 '''

import sys
import re

INSTRUCTION = re.compile(r'(?P<op>turn off|turn on|toggle) (?P<x1>[0-9]*),(?P<y1>[0-9]*) '
                         r'through (?P<x2>[0-9]*),(?P<y2>[0-9]*)')

INPUT = __file__.replace('advent_', 'input_').replace('py', 'txt')

def get_input():
    ''' Read puzzle input '''
    with open(INPUT, 'r', encoding='utf-8') as file:
        for line in file:
            d = INSTRUCTION.match(line).groupdict()
            yield (d['op'],
                   min(int(d['x1']), int(d['x2'])),
                   max(int(d['x1']), int(d['x2'])) + 1,
                   min(int(d['y1']), int(d['y2'])),
                   max(int(d['y1']), int(d['y2'])) + 1)

def main():
    ''' main '''
    part1 = 0
    part2 = 0
    lights = [[False for _ in range(1000)].copy() for _ in range(1000)]
    lights2 = [[0 for _ in range(1000)].copy() for _ in range(1000)]
    for index, (op, x1, x2, y1, y2) in enumerate(get_input(), 1):
        for x in range(x1, x2):
            for y in range(y1, y2):
                # Part 1
                if lights[x][y]:
                    if op == 'turn off' or op == 'toggle':
                        lights[x][y] = False
                        part1 -= 1
                else:
                    if op == 'turn on' or op == 'toggle':
                        lights[x][y] = True
                        part1 += 1

                # Part 2
                if op == 'turn on':
                    lights2[x][y] += 1
                    part2 += 1
                elif op == 'turn off':
                    if lights2[x][y] > 0:
                        lights2[x][y] -= 1
                        part2 -= 1
                else:
                    lights2[x][y] += 2
                    part2 += 2

    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
