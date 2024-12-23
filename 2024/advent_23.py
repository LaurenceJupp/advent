#!/usr/bin/env python3
''' https://adventofcode.com/2024/day/23 '''

from collections import defaultdict
from itertools import combinations
from functools import cache

INPUT = 'input_23.txt'

@cache
def get_input():
    ''' Return input as dictionary of linked computers '''
    connections = defaultdict(list)
    with open(INPUT, 'r', encoding='utf-8') as input23:
        for line in input23:
            computers = line.strip().split('-')
            connections[computers[0]].append(computers[1])
            connections[computers[1]].append(computers[0])
    return connections

def get_subsets(computers):
    ''' Return length - 1 subsets '''
    for index in range(len(computers)):
        yield computers[:index] + computers[index + 1:]

@cache
def is_connected(computers):
    ''' Return length of max connected set plus an example '''
    length = len(computers)
    if length == 2:
        return (2, computers) if computers[0] in get_input()[computers[1]] else (0, tuple())

    max_length = 0
    all_valid = True
    for subset in get_subsets(computers):
        group_length, group = is_connected(subset)
        if group_length >= max_length:
            max_length = group_length
            max_group = group
        if group_length != length - 1:
            all_valid = False
    return (length, computers) if all_valid else (max_length, max_group)

def main():
    ''' main '''
    valid_threes = set()
    password_length = 0
    for first, others in get_input().items():
        computers = tuple(sorted(others + [first]))
        for three in combinations(computers, 3):
            if any(c[0] == 't' for c in three) and is_connected(three)[0] == 3:
                valid_threes.add(three)
        new_password_length, new_password = is_connected(computers)
        if new_password_length > password_length:
            password_length = new_password_length
            password = new_password
    print(f'Part 1: {len(valid_threes)}')
    print(f'Part 2: {','.join(password)}')

main()
