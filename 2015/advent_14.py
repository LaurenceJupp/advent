#!/usr/bin/env python3
''' https://adventofcode.com/2015/day/14 '''

import sys

RACE_TIME = 2503
INPUT = __file__.replace('advent_', 'input_').replace('py', 'txt')

def get_input():
    ''' Yield puzzle input as tuples '''
    with open(INPUT, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.split()
            yield int(word[3]), int(word[6]), int(word[13])

def distance(race_time, flight_speed, flight_time, rest_time):
    ''' Calculate reindeer distance '''
    return flight_speed * (flight_time * (race_time // (flight_time + rest_time)) +
                           min(flight_time, race_time % (flight_time + rest_time)))

def main():
    ''' main '''
    puzzle = tuple(get_input())

    print(f'Part 1: {max(distance(RACE_TIME, *x) for x in puzzle)}')

    # Part 2
    points = [0 for _ in puzzle]
    for race_time in range(1, RACE_TIME + 1):
        distances = tuple(distance(race_time, *x) for x in puzzle)
        maximum = max(distances)
        for i, dist in enumerate(distances):
            if dist == maximum:
                points[i] += 1
    print(f'Part 2: {max(points)}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
