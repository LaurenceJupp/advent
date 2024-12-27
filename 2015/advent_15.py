#!/usr/bin/env python3
''' https://adventofcode.com/2015/day/15 '''

import sys

INPUT = __file__.replace('advent_', 'input_').replace('py', 'txt')
CALORIES = -1

def get_input():
    ''' Yield puzzle input as tuples '''
    with open(INPUT, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.replace(',','').split()
            yield tuple(int(word[i]) for i in range(2,11,2))

def quality(quantity, puzzle, quality_index):
    ''' Calculate score for this particular quality index '''
    return sum(quantity[i] * puzzle[i][quality_index] for i in range(len(puzzle)))

def score(quantity, puzzle, calories=None):
    ''' Calculate total score for this set of quantities '''
    total = 1
    for quality_index in range(len(puzzle[0]) - 1):
        total *= max(quality(quantity, puzzle, quality_index), 0)
    return 0 if calories is not None and quality(quantity, puzzle, CALORIES) != calories else total

def amounts(num, total):
    ''' Generate all combinations of num amounts summing to total '''
    if num == 1:
        yield (total,)
    else:
        for i in range(total + 1):
            for other in amounts(num - 1, total - i):
                yield (i,) + other

def main():
    ''' main '''
    puzzle = tuple(get_input())
    print(f'Part 1: {max(score(quantity, puzzle) for quantity in amounts(len(puzzle), 100))}')
    print(f'Part 2: {max(score(quantity, puzzle, calories=500)
          for quantity in amounts(len(puzzle), 100))}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
