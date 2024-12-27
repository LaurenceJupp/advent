#!/usr/bin/env python3
''' https://adventofcode.com/2015/day/12 '''

import sys
import json

INPUT = __file__.replace('advent_', 'input_').replace('py', 'txt')

def get_input():
    ''' Read puzzle input as json '''
    with open(INPUT, 'r', encoding='utf-8') as file:
        return json.load(file)

def parse(obj, avoid):
    ''' Parse object - according to rules of part 2 if avoid is 'red' '''
    match obj:
        case int():
            return obj
        case list():
            return sum(parse(x, avoid) for x in obj)
        case dict():
            items = [*obj.keys(), *obj.values()]
            return 0 if avoid is not None and avoid in items else parse(items, avoid)
    return 0

def main():
    ''' main '''
    puzzle = get_input()
    print(f'Part 1: {parse(puzzle, avoid=None)}')
    print(f'Part 2: {parse(puzzle, avoid="red")}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
