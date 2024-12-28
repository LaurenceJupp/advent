#!/usr/bin/env python3
''' https://adventofcode.com/2015/day/21 '''

import sys
from itertools import combinations

# Boss
BOSS_HP = 103
BOSS_DAMAGE = 9
BOSS_ARMOR = 2

# Me
ME_HP = 100

SHOP = '''
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
None          0     0       0
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
None          0     0       0
None          0     0       0
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
'''

def get_shop():
    ''' Parse SHOP '''
    weapons = []
    armors = []
    rings = []
    item = None
    for line in SHOP.splitlines():
        match line[:8]:
            case 'Weapons:':
                item = weapons
            case 'Armor:  ':
                item = armors
            case 'Rings:  ':
                item = rings
            case _:
                if line:
                    c = int(line[12:15].strip())
                    d = int(line[20])
                    a = int(line[28])
                    item.append((c, d, a))
    return weapons, armors, rings

def main():
    ''' main '''
    weapons, armors, rings = get_shop()

    victory_cost = 1000
    loss_cost = 0
    for w in weapons:
        for a in armors:
            for r1, r2 in combinations(rings, 2):
                cost, damage, armor = (sum(x) for x in zip(w, a, r1, r2))
                attack = max(damage - BOSS_ARMOR, 1)
                defend = max(BOSS_DAMAGE - armor, 1)
                if (BOSS_HP + attack - 1) // attack <= (ME_HP + defend - 1) // defend:
                    if cost < victory_cost:
                        victory_cost = cost
                elif cost > loss_cost:
                    loss_cost = cost
    print(f'Part 1: {victory_cost}')
    print(f'Part 2: {loss_cost}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
