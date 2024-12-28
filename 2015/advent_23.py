#!/usr/bin/env python3
''' https://adventofcode.com/####/day/# '''

import sys

INPUT = __file__.replace('advent_', 'input_').replace('py', 'txt')

def get_input():
    ''' Read puzzle input '''
    with open(INPUT, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.split()
            line[1] = line[1].replace(',', '')
            try:
                line[1] = int(line[1])
            except ValueError:
                pass
            try:
                line[2] = int(line[2])
            except IndexError:
                pass
            yield line

def run(text, reg, pc):
    while 0 <= pc < len(text):
        print(f"{reg['a']}, {reg['b']}")
        opcode = text[pc][0]
        arg1 = text[pc][1]
        match opcode:
            case 'hlf':
                reg[arg1] //= 2
            case 'tpl':
                reg[arg1] *= 3
            case 'inc':
                reg[arg1] += 1
            case 'jmp':
                pc += arg1 - 1
            case 'jie':
                if (reg[arg1] & 1) == 0:
                    pc += text[pc][2] - 1
            case 'jio':
                if reg[arg1] == 1:
                    pc += text[pc][2] - 1
        pc += 1

def main():
    ''' main '''
    for i in range(2):
        text = tuple(get_input())
        reg = {'a': i, 'b': 0}
        pc = 0
        run(text, reg, pc)
        print(f'Part {i + 1}: {reg["b"]}')

    return 0

if __name__ == '__main__':
    sys.exit(main())
