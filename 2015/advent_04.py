#!/usr/bin/env python3
''' https://adventofcode.com/2015/day/4 '''

import sys
from hashlib import md5

INPUT = 'iwrupvqb'

def main():
    ''' main '''
    part1 = True
    for i in range(sys.maxsize):
        m = md5(f'{INPUT}{i}'.encode('utf-8')).hexdigest()
        if part1 and m.startswith('00000'):
            print(f'Part 1: {i}')
            part1 = False
        if m.startswith('000000'):
            print(f'Part 2: {i}')
            return 0

if __name__ == '__main__':
    sys.exit(main())
