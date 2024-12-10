from itertools import combinations


def read_and_parse_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    containers = list(map(int, lines))

    return containers


def calculate_capacity(combination, containers):
    capacity = 0

    for i in combination:
        capacity += containers[i]

    return capacity


def solve():
    containers = read_and_parse_file('input.txt')
    liters = 150

    combos = []

    for i in range(len(containers)):
        for combo in combinations(containers, i):
            if sum(combo) == liters:
                combos.append(combo)

    print(f'{len(combos)} combinations can fit {liters} liters of eggnog')

    min_amount = min(map(len, combos))
    minimal_combos = list(filter(lambda c: len(c) == min_amount, combos))

    print(f'{len(minimal_combos)} combinations can fit {liters} liters of eggnog with {min_amount} containers')


solve()
