#!/usr/bin/env python3
''' Advent of Code 2024 Day 21 '''
from functools import cache

#INPUT = ('029A', '980A', '179A', '456A', '379A')
INPUT = ('341A', '480A', '286A', '579A', '149A')
# Coordinates of each key
NUMMAP = {'0': (1,0), '1': (0,1), '2': (1,1), '3': (2,1), '4': (0,2), '5': (1,2),
          '6': (2,2), '7': (0,3), '8': (1,3), '9': (2,3), 'A': (2,0)}
DIRMAP = {'<': (0,0), 'v': (1,0), '>': (2,0), '^': (1,1), 'A': (2,1)}

def get_sequences(start, end, missing):
    ''' Sequences of key-presses to get robot from start key to press end key '''
    # Vector from start to end
    diff = (end[0] - start[0], end[1] - start[1])
    # string of key-presses to move horizontally
    hor = ('>' if diff[0] > 0 else '<') * abs(diff[0])
    # string of key-presses to move vertically
    ver = ('^' if diff[1] > 0 else 'v') * abs(diff[1])
    # Return set of all valid strings of key-presses
    return (set({ver + hor + 'A'} if (start[0], end[1]) != missing else {}) |
            set({hor + ver + 'A'} if (end[0], start[1]) != missing else {}))

def get_total_length(sequence, num_levels, level=0):
    ''' Minimum number of key-presses for sequence through (num_levels - level) robots '''
    # Always start at 'A' - but it's not part of the sequence to enter
    seq = 'A' + sequence
    return sum(get_length(seq[i], seq[i+1], num_levels, level) for i in range(len(seq) - 1))

@cache
def get_length(old, new, num_levels, level):
    ''' Minimum number of key-presses from old to press new through (num_levels - level) robots '''
    args = (NUMMAP[old], NUMMAP[new], (0,0)) if level == 0 else (DIRMAP[old], DIRMAP[new], (0,1))
    # Either return the length of the sequences, or do further recursion
    return (len(next(iter(get_sequences(*args)))) if level == num_levels else
            min(get_total_length(s, num_levels, level=level+1) for s in get_sequences(*args)))

def main():
    ''' main '''
    for part, num_levels in (1, 2), (2, 25):
        total_score = sum(get_total_length(code, num_levels) * int(code[:-1]) for code in INPUT)
        print(f'Part {part}: {total_score}')
main()