#!/usr/bin/env python3
''' https://adventofcode.com/2024/day/24 '''

import re

RANDOM_SUM_CHECKS = False
if RANDOM_SUM_CHECKS:
    from random import randint

INPUT = 'input_24.txt'
RE_INPUT = re.compile(r'(?P<wire>[xy][0-9]{2}): (?P<value>[01])|'
                      r'(?P<in1>[a-z0-9]{3}) (?P<op>AND|OR|XOR) '
                      r'(?P<in2>[a-z0-9]{3}) -> (?P<out>[a-z0-9]{3})')

def get_input():
    ''' Input as dictionaries of reset values and gate recipes '''
    with open(INPUT, 'r', encoding='utf-8') as input24:
        init = {}
        recipe = {}
        for line in input24:
            match = RE_INPUT.match(line)
            if match:
                if match['wire']:
                    init[match['wire']] = int(match['value'])
                else:
                    recipe[match['out']] = (match['op'], match['in1'], match['in2'])
        return init, recipe

def get_wire(item, init, recipe):
    ''' Determine level on wire '''
    if item in init:
        return init[item]

    in1 = get_wire(recipe[item][1], init, recipe)
    in2 = get_wire(recipe[item][2], init, recipe)
    operation = recipe[item][0]

    if operation == 'AND':
        return in1 & in2
    if operation == 'OR':
        return in1 | in2
    if operation == 'XOR':
        return in1 ^ in2

    print('Bad')
    return None

def reg(char, init, recipe):
    ''' Return x, y or z register components as tuple '''
    all_regs = tuple(recipe.keys()) + tuple(init.keys())
    return sorted([x for x in all_regs if x[0] == char], reverse=True)

def find_gate(recipe, operator, operands, swaps):
    ''' Find gate in recipe, returning key and updating 'swaps' if necessary '''
    for key, values in recipe.items():
        recipe_operands = {values[1], values[2]}
        if values[0] == operator and recipe_operands == operands:
            # Recipe for this gate appears to be good
            return key
        difference = recipe_operands - operands
        if len(difference) == 1:
            # One of the wires is wrong
            (wire1,) = difference
            (wire2,) = operands - recipe_operands
            # Add entries for both directions
            if not swaps:
                swaps[wire1] = wire2
                swaps[wire2] = wire1
            return key
    # Should never get here
    print('Bad', operator, operands)
    return None

def check_adder(recipe_start, regx, regy):
    '''
    Construct adder based on gates in recipe_start but correcting
    swapped wires as we go to end up with a working recipe

    # G1 = XOR(X, Y)
    # G2 = AND(X, Y)
    # G3 = XOR(G1, C)
    # G4 = AND(G1, C)
    # G5 = OR(G2, G4)
    #
    # Z = G3
    # C = G5
    '''
    # Accumulate record of swapped wires as double-direction dictionary
    all_swaps = {}
    # Loop while we're still swapping
    while True:
        # Update recipe_start with all_swaps
        recipe = {}
        for key, values in recipe_start.items():
            recipe[all_swaps.get(key, key)] = values
        # Loop over bits, from 0, confirming each gate
        carry = None
        swaps = {}
        for count, (x, y) in enumerate(zip(reversed(regx), reversed(regy))):
            gate1 = find_gate(recipe, 'XOR', {x, y}, swaps)
            gate2 = find_gate(recipe, 'AND', {x, y}, swaps)
            if carry:
                # Full adder for later bits
                gate3 = find_gate(recipe, 'XOR', {gate1, carry}, swaps)
                gate4 = find_gate(recipe, 'AND', {gate1, carry}, swaps)
                gate5 = find_gate(recipe, 'OR', {gate2, gate4}, swaps)
                z = gate3
                carry = gate5
            else:
                # No input carry on first bit, so half-adder
                z = gate1
                carry = gate2

            if swaps:
                all_swaps |= swaps
                # A swap requires a restart
                break

            if z != z.replace('x','z'):
                # Should never get here
                print('Bad')
        else:
            # All done without any further swaps
            break

    # Make sure the final carry ends up in the top bit of Z
    if carry != f'z{count + 1:2}':
        # Should never get here
        print('Bad')

    return all_swaps, recipe

def check_recipe(first, second, recipe, regz):
    ''' Checks the sum of first and second, according to recipe '''
    init = {}
    for register, value in ('x', first), ('y', second):
        for index, bit in enumerate(reversed(f'{value:045b}')):
            init[f'{register}{index:02}'] = int(bit)
    recipe_sum = int(''.join(str(get_wire(z, init, recipe)) for z in regz), 2)
    return recipe_sum == sum((first, second))

def main():
    ''' Advent of Code 2024 Day 24 '''
    init, recipe = get_input()

    regx = reg('x', init, recipe)
    regy = reg('y', init, recipe)
    regz = reg('z', init, recipe)
    swaps, fixed_recipe = check_adder(recipe, regx, regy)

    print(f'Part 1: {int(''.join(str(get_wire(z, init, recipe)) for z in regz), 2)}')
    print(f'Part 2: {','.join(sorted(swaps.keys()))}')

    if RANDOM_SUM_CHECKS:
        for index in range(20000):
            if (index & 0x3FF) == 0:
                print(f'Random check number {index} of 20000')
            rand = tuple(randint(0, (1 << 45) - 1) for _ in range(2))
            if not check_recipe(*rand, fixed_recipe, regz):
                print('Bad', rand)
                break
        else:
            print('All passed')
main()
