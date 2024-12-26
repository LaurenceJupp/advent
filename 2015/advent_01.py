#!/usr/bin/env python3
''' https://adventofcode.com/2015/day/1 '''

INPUT = 'input_01.txt'

def get_input():
    ''' Return input as string '''
    with open(INPUT, 'r', encoding='utf-8') as input01:
        return input01.read().strip()

def main():
    ''' Count parentheses and then detect basement move '''
    lisp = get_input()
    print(f'Part 1: {lisp.count('(') - lisp.count(')')}')
    floor = 0
    for position, char in enumerate(lisp, 1):
        floor += 1 if char == '(' else -1
        if floor == -1:
            print(f'Part 2: {position}')
            break


main()
