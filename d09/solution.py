from itertools import permutations


def read_and_parse_file(file_path):
    graph = {}

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(" ")

            city1 = parts[0]
            city2 = parts[2]
            distance = int(parts[4])

            if city1 not in graph:
                graph[city1] = {}

            if city2 not in graph:
                graph[city2] = {}

            graph[city1][city2] = distance
            graph[city2][city1] = distance

    return graph


def calculate_longest_distance(graph):
    cities = graph.keys()
    routes = list(permutations(cities))

    longest_distance = 0

    for route in routes:
        current_distance = 0

        for i in range(len(cities) - 1):
            current_distance += graph[route[i]][route[i + 1]]

        if current_distance > longest_distance:
            longest_distance = current_distance

    return longest_distance


def calculate_shortest_distance(graph):
    cities = graph.keys()
    routes = list(permutations(cities))

    shortest_distance = 10 ** 100  # practically infinite

    for route in routes:
        current_distance = 0

        for i in range(len(cities) - 1):
            current_distance += graph[route[i]][route[i + 1]]

        if current_distance < shortest_distance:
            shortest_distance = current_distance

    return shortest_distance


def solve():
    graph = read_and_parse_file('input.txt')

    shortest_distance = calculate_shortest_distance(graph)

    print(f'The shortest distance to visit all cities is {shortest_distance}')

    longest_distance = calculate_longest_distance(graph)

    print(f'The longest distance to visit all cities is {longest_distance}')


solve()
