#!/usr/bin/env python3
''' https://adventofcode.com/2015/day/19 '''

import sys
from collections import defaultdict

INPUT = __file__.replace('advent_', 'input_').replace('py', 'txt')

def get_input():
    ''' Puzzle input as dictionary of recipes and molecule string '''
    recipes = defaultdict(list)
    with open(INPUT, 'r', encoding='utf-8') as file:
        for line in file:
            if line := line.strip():
                try:
                    key, value = line.strip().split(' => ')
                    recipes[key].append(value)
                except ValueError:
                    return recipes, line
    print('get_input failed')
    sys.exit(1)

def distinct(molecule, recipes):
    ''' Return set of distinct molecules after 1 step '''
    new_molecules = set()
    for i, _ in enumerate(molecule):
        for key, values in recipes.items():
            if molecule[i:].startswith(key):
                for v in values:
                    new_molecules.add(molecule[:i] + v + molecule[i + len(key):])
    return len(new_molecules)

def get_elements(recipes):
    ''' Return sorted lists of all elements and also stable elements that cannot change '''
    elements = set()
    for values in recipes.values():
        for v in values:
            while v:
                # Two-letter element
                if v[-1].islower():
                    elements.add(v[-2:])
                    v = v[:-2]
                else:
                    # Single-letter element
                    elements.add(v[-1])
                    v = v[:-1]
    stable = elements - set(recipes.keys())
    return sorted(list(elements)), sorted(list(stable))

def get_stable_pattern(molecule, elements, stable):
    '''
    Returns a string showing indices of stable elements in molecule
    Unstable elements are regarded as interchangeable and so they
    are all just represented as '.'s
    '''
    pattern = ''
    while molecule:
        if molecule[:2] in elements:
            # Two-letter element
            if molecule[:2] in stable:
                pattern += str(stable.index(molecule[:2]))
            else:
                pattern += '.'
            molecule = molecule[2:]
        else:
            # Single-letter element
            if molecule[0] in stable:
                pattern += str(stable.index(molecule[0]))
            else:
                pattern += '.'
            molecule = molecule[1:]
    return pattern

def main():
    ''' main '''
    recipes, molecule = get_input()

    print('Sample1', distinct('HOH', {'H': ['HO', 'OH'], 'O': ['HH']}))
    print('Sample2', distinct('HOHOHO', {'H': ['HO', 'OH'], 'O': ['HH']}))

    print(f'Part 1: {distinct(molecule, recipes)}')

    # The idea for Part 2 is that there are 'stable' elements that cannot be altered
    # once they are created. If you look at the recipes, you can also see that there's
    # only a finite set of patterns of unstable and individual stable elements produced
    # from any unstable element. This means that we can just match those patterns in the
    # required molecule and replace them with an unstable element for each step. (Unstable
    # elements are completely interchangeable as far as the patterns are concerned, so they
    # get replaced by '.'. Stable elements are unique and so are numbered.
    # So all we do is find all of the patterns and then count replacements in the molecule
    # until we are reduced to a single unstable element - which must be 'e'.
    elements, stable = get_elements(recipes)
    molecule_pattern = get_stable_pattern(molecule, elements, stable)

    # Set of all output patterns for the recipes
    blocks = set(get_stable_pattern(x, elements, stable) for v in recipes.values() for x in v)

    # Replace output patterns with a single unstable element until we are back to just '.'
    count = 0
    while molecule_pattern != '.':
        for block in blocks:
            if block in molecule_pattern:
                molecule_pattern = molecule_pattern.replace(block, '.', 1)
                count += 1
    print(f'Part 2: {count}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
