#!/usr/bin/env python3
''' https://adventofcode.com/2015/day/7 '''

import sys
import re
from functools import cache

INSTRUCTION = re.compile(r'(?P<arg1>[a-z0-9]*)?\s?(?P<op>NOT|AND|OR|[LR]SHIFT)?\s'
                         r'?(?P<arg2>[a-z0-9]*)\s->\s(?P<out>[a-z]*)')
INPUT = __file__.replace('advent_', 'input_').replace('py', 'txt')

@cache
def get_input(b=None):
    ''' Read puzzle input as dictionary. Override b if not None (for part 2) '''
    with open(INPUT, 'r', encoding='utf-8') as file:
        rules = {}
        for line in file:
            d = INSTRUCTION.match(line).groupdict()
            rules[d['out']] = d
    if not b is None:
        rules['b']['arg1'] = str(b)
    return rules

@cache
def get_value(item, b):
    ''' Determine value of item. b is just passed through to get_input() '''
    if item.isdigit():
        return int(item)

    rules = get_input(b)
    match rules[item]['op']:
        case 'NOT':
            return ~get_value(rules[item]['arg2'], b) & 0xFFFF
        case 'AND':
            return get_value(rules[item]['arg1'], b) & get_value(rules[item]['arg2'], b)
        case 'OR':
            return get_value(rules[item]['arg1'], b) | get_value(rules[item]['arg2'], b)
        case 'LSHIFT':
            return get_value(rules[item]['arg1'], b) << get_value(rules[item]['arg2'], b)
        case 'RSHIFT':
            return get_value(rules[item]['arg1'], b) >> get_value(rules[item]['arg2'], b)
        case None:
            return get_value(rules[item]['arg1'], b)
        case default:
            print('Bad')
            sys.exit(1)
            return None

def main():
    ''' main '''
    part1 = get_value('a', b=None)
    print(f'Part 1: {part1}')
    part2 = get_value('a', b=part1)
    print(f'Part 2: {part2}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
