#!/usr/bin/env python3
''' https://adventofcode.com/2015/day/25 '''

import sys

INPUT = (3029, 2947)
START = 20151125
MULT = 252533
MODULO = 33554393

def linear_position(x, y):
    ''' Turn (x, y) coords into a linear index '''
    return (x + y - 1) * (x + y - 2) // 2 + x

def main():
    ''' main '''
    code = START
    for _ in range(linear_position(*INPUT) - 1):
        code *= MULT
        code %= MODULO

    print(f'Part 1: {code}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
