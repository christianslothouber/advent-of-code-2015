weapons = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0)
]

armors = [
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
    (0, 0, 0)
]

rings = [
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
    (0, 0, 0),
    (0, 0, 0)
]


def generate_load_outs():
    load_outs = []

    for w in range(len(weapons)):
        for a in range(len(armors)):
            for r1 in range(len(rings)):
                for r2 in range(len(rings)):
                    load_out = (w, a, r1, r2)
                    load_outs.append(load_out)

    return set(load_outs)


def calculate_load_out(load_out):
    hp = 100
    damage = 0
    armor = 0
    cost = 0

    selected_weapon = weapons[load_out[0]]
    selected_armor = armors[load_out[1]]
    selected_ring_1 = rings[load_out[2]]
    selected_ring_2 = rings[load_out[3]]

    cost += selected_weapon[0]
    cost += selected_armor[0]
    cost += selected_ring_1[0]
    cost += selected_ring_2[0]

    damage += selected_weapon[1]
    damage += selected_armor[1]
    damage += selected_ring_1[1]
    damage += selected_ring_2[1]

    armor += selected_weapon[2]
    armor += selected_armor[2]
    armor += selected_ring_1[2]
    armor += selected_ring_2[2]

    return hp, damage, armor, cost


def fight(stats):
    boss_hp = 104
    boss_damage = 8
    boss_armor = 1

    hp, damage, armor, cost = stats

    while hp > 0:
        actual_damage = max(1, damage - boss_armor)
        boss_hp -= actual_damage

        if boss_hp <= 0:
            return True

        actual_damage = max(1, boss_damage - armor)
        hp -= actual_damage

    return False


def solve():
    load_outs = generate_load_outs()
    stats = list(map(calculate_load_out, load_outs))

    won = list(filter(fight, stats))
    price = min(map(lambda w: w[3], won))
    print(f'Cheapest load out that wins costs {price}')

    lost = list(filter(lambda s: not fight(s), stats))
    price = max(map(lambda w: w[3], lost))
    print(f'Most expensive load out that loses costs {price}')


solve()
