#!/usr/bin/env python3
''' https://adventofcode.com/2015/day/11 '''

import sys

INPUT = 'cqjxjnds'

def base26_to_decimal(b26):
    ''' Convert base26 to decimal '''
    return sum((ord(char) - ord('a')) * 26 ** index for index, char in enumerate(reversed(b26)))

def decimal_to_tuple(dec):
    ''' Convert decimal to tuple of base26 digits as decimals '''
    return tuple((dec // (26 ** i)) % 26 for i in range(7, -1, -1))

def decimal_to_base26(dec):
    ''' Convert decimal to base26 '''
    return ''.join(chr(x + ord('a')) for x in decimal_to_tuple(dec))

def validate(dec):
    ''' Validate decimal version of passwrd '''
    # tuple of base26 digits as decimals
    sequence = decimal_to_tuple(dec)

    # Must not contain i, o, l
    if any(ord(x) - ord('a') in sequence for x in 'iol'):
        return False

    # Must contain two pairs
    pair_count = 0
    for i in range(7):
        if (i == 0 or sequence[i-1] != sequence[i]) and sequence[i] == sequence[i+1]:
            if (pair_count := pair_count + 1) == 2:
                break
    else:
        return False

    # Must contain a run of three
    for i in range(6):
        if sequence[i + 1] == sequence[i] + 1 and sequence[i + 2] == sequence[i + 1] + 1:
            break
    else:
        return False

    # Passed
    return True

def main():
    ''' main '''
    current = base26_to_decimal(INPUT) + 1
    while not validate(current):
        current += 1
    print(f'Part 1: {decimal_to_base26(current)}')

    current += 1
    while not validate(current):
        current += 1
    print(f'Part 2: {decimal_to_base26(current)}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
