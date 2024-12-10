from itertools import product
import re


def read_and_parse_file(file_path):
    with open(file_path, 'r') as file:
        ingredients = {line.split(':')[0]: tuple(map(int, re.findall(r'-?\d+', line))) for line in file}

    return ingredients


def find_permutations(n, m):
    permutations = []

    for combination in product(range(m + 1), repeat=n):
        if sum(combination) == m:
            permutations.append(list(combination))

    return permutations


def calculate_score(recipe, ingredients, restrict_diet):
    bowls = []

    for index, ingredient in enumerate(ingredients.values()):
        spoon = recipe[index]
        bowl = tuple(spoon * property for property in ingredient)

        bowls.append(bowl)

    bowl = tuple(map(sum, zip(*bowls)))
    bowl = tuple(0 if property < 0 else property for property in bowl)

    if restrict_diet and bowl[4] != 500:
        return 0

    score = bowl[0] * bowl[1] * bowl[2] * bowl[3]

    return score


def solve():
    ingredients = read_and_parse_file('input.txt')
    recipes = find_permutations(len(ingredients), 100)

    scores = list(map(lambda recipe: calculate_score(recipe, ingredients, False), recipes))
    print(f'Max score is {max(scores)}')

    scores = list(map(lambda recipe: calculate_score(recipe, ingredients, True), recipes))
    print(f'Max score with diet restriction is {max(scores)}')


solve()
