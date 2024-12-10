from itertools import permutations


def read_and_parse_file(file_path):
    graph = {}

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip('.\n').split(" ")

            person1 = parts[0]
            person2 = parts[10]
            happiness = int(parts[3])

            if parts[2] == 'lose':
                happiness *= -1

            if person1 not in graph:
                graph[person1] = {}

            graph[person1][person2] = happiness

    return graph


def calculate_happiness(arrangement, graph):
    happiness = 0

    for i in range(len(arrangement)):
        person = arrangement[i]

        person_left = arrangement[i - 1]
        happiness += graph[person][person_left]

        person_right = arrangement[(i + 1) % len(arrangement)]
        happiness += graph[person][person_right]

    return happiness


def calculate_max_happiness(graph):
    arrangements = list(permutations(graph.keys()))
    max_happiness = max(map(lambda arrangement: calculate_happiness(arrangement, graph), arrangements))

    return max_happiness


def add_tommy(graph):
    graph['Tommy'] = {}

    for person in graph.keys():
        if person != 'Tommy':
            graph['Tommy'][person] = 0
            graph[person]['Tommy'] = 0


def solve():
    graph = read_and_parse_file('input.txt')

    max_happiness = calculate_max_happiness(graph)

    print(f'The total change in happiness is {max_happiness}')

    add_tommy(graph)
    max_happiness = calculate_max_happiness(graph)

    print(f'The total change in happiness with me is {max_happiness}')


solve()
