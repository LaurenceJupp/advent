#!/usr/bin/env python3
''' https://adventofcode.com/2024/day/24 '''

import re

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
                    recipe[match['out']] = [match['op'], match['in1'], match['in2']]
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

def suspicious_wires(recipe, regx, regy, regz):
    ''' Work out which wires are not as expected in our adder '''
    bad = []
    for bit in range(3, len(regz)):
        # 5 gates to check
        xor_final = recipe[regz[-bit]]
        # Z = Gate1 = Gate2 XOR Gate3
        if xor_final[0] != 'XOR':
            bad.append(regz[-bit])
            continue
        for wire1, recipe1 in ((x, (recipe[x] if x in recipe else x)) for x in xor_final[1:]):
            # Gate2 = X XOR Y
            if recipe1[0] == 'XOR' and set(recipe1[1:]) == set({regx[-bit], regy[-bit]}):
                continue
            # Gate3 = Gate4 OR Gate5
            if recipe1[0] != 'OR':
                bad.append(wire1)
                break
            # Gates 4/5 are X' AND Y or previous final gate but AND instead of XOR
            for wire2, recipe2 in ((x, recipe[x]) for x in recipe1[1:]):
                if (recipe2[0] != 'AND' or
                    (set(recipe2[1:]) != set({regx[-bit+1], regy[-bit+1]}) and
                     set(recipe2[1:]) != set(recipe[regz[-bit+1]][1:]))):
                    bad.append(wire2)
                    break
    return bad

def main():
    ''' Advent of Code 2024 Day 24 '''
    init, recipe = get_input()

    regx = reg('x', init, recipe)
    regy = reg('y', init, recipe)
    regz = reg('z', init, recipe)

    print(f'Part 1: {int(''.join(str(get_wire(x, init, recipe)) for x in regz), 2)}')
    print(f'Part 2: {','.join(sorted(suspicious_wires(recipe, regx, regy, regz)))}')

main()
