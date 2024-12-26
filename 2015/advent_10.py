#!/usr/bin/env python3
''' https://adventofcode.com/2015/day/10 '''

import sys

INPUT = '1321131112'

def looksay(string, countdown):
    ''' Recursive https://en.wikipedia.org/wiki/Look-and-say_sequence '''
    new = ''
    dig = '0'
    run = 0
    for i, char in enumerate(string):
        if char == dig:
            run += 1
        else:
            if i != 0:
                new += str(run) + dig
            dig = char
            run = 1
    new += str(run) + dig
    return new if (countdown := countdown - 1) == 0 else looksay(new, countdown)

def main():
    ''' main '''
    part1 = looksay(INPUT, 40)
    print(f'Part 1: {len(part1)}')
    print(f'Part 2: {len(looksay(part1, 10))}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
