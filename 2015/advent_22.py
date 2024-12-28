#!/usr/bin/env python3
''' https://adventofcode.com/2015/day/22 '''

import sys

# Boss
BOSS_HP = 58
BOSS_DAMAGE = 9

# Me
ME_HP = 50
ME_MANA = 500

#Spells - Cost, damage, heal, shield, recharge
SPELLS = [(53,  4,      0,    0,      0,        'Magic Missile'),
          (73,  2,      2,    0,      0,        'Drain'),
          (113, 0,      0,    (7, 6), 0,        'Shield'),
          (173, (3, 6), 0,    0,      0,        'Poison'),
          (229, 0,      0,    0,      (101, 5), 'Recharge')]

def effect(e):
    ''' Manage timer effect '''
    if not e:
        return 0, 0
    new_e = (e[0], e[1] - 1) if e[1] > 1 else 0
    return e[0], new_e

def our_turn(state, spell):
    ''' One of our turns in the game '''
    # Hard difficulty and mana accounting
    state['hp'] -= state['hard']
    state['mana'] -= spell[0]
    state['mana_used'] += spell[0]
    if (state['hp'] <= 0 or
        state['mana'] < 0 or
        state['mana_limit'] and state['mana_used'] > state['mana_limit']):
        return []

    # Damage from spell
    try:
        state['boss_hp'] -= spell[1]
    except TypeError:
        # Poison - not instant
        if state['damage']:
            # Can't poison twice
            return []
        state['damage'] = spell[1]

    # Healing from spell
    state['hp'] += spell[2]

    # Shield spell
    if spell[3]:
        if state['shield']:
            # Can't shield twice
            return []
        state['shield'] = spell[3]

    # Recharge spell
    if spell[4]:
        if state['recharge']:
            # Can't recharge twice
            return []
        state['recharge'] = spell[4]

    if state['boss_hp'] <= 0:
        if not state['mana_limit'] or state['mana_used'] < state['mana_limit']:
            state['mana_limit'] = state['mana_used']
        return [state]

    # Boss turn next
    return turn(state, None)

def turn(state, spell):
    ''' One turn of the game '''
    state['turn'] += 1

    # Effect timers
    shield, state['shield'] = effect(state['shield'])
    damage, state['damage'] = effect(state['damage'])
    state['boss_hp'] -= damage
    recharge, state['recharge'] = effect(state['recharge'])
    state['mana'] += recharge

    if spell: # Our turn
        return our_turn(state, spell)

    if state['boss_hp'] <= 0:
        if not state['mana_limit'] or state['mana_used'] < state['mana_limit']:
            state['mana_limit'] = state['mana_used']
        return [state]

    # Boss turn
    state['hp'] -= max(BOSS_DAMAGE - shield, 1)
    if state['hp'] <= 0:
        return []

    # Our turn next, so choose spell
    for s in SPELLS:
        for child_state in turn(state.copy(), s):
            if not state['mana_limit'] or child_state['mana_limit'] < state['mana_limit']:
                state['mana_limit'] = child_state['mana_limit']
    if state['mana_limit']:
        return[state]
    return []

def main():
    ''' main '''

    # Game state
    state = {'turn': 0,
             'hp': ME_HP,
             'mana': ME_MANA,
             'shield': 0,
             'damage': 0,
             'recharge': 0,
             'boss_hp': BOSS_HP,
             'mana_used': 0,
             'hard': 0,
             'mana_limit': None}

    # Play part 1
    part1 = min(turn(state.copy(), s)[0]['mana_limit'] for s in SPELLS)
    print(f'Part 1: {part1}')

    # Play part 2
    state['hard'] = 1
    part2 = min(turn(state.copy(), s)[0]['mana_limit'] for s in SPELLS)
    print(f'Part 2: {part2}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
