def read_and_parse_file(file_path):
    with open(file_path, 'r') as file:
        instructions = file.read()

    return instructions


def find_visited_houses(instructions):
    x = 0
    y = 0

    houses = {x, y}

    for instruction in instructions:
        if instruction == '>':
            x += 1
        if instruction == '<':
            x -= 1
        if instruction == '^':
            y += 1
        if instruction == 'v':
            y -= 1

        house = (x, y)

        houses.add(house)

    return houses


def find_visited_houses_with_robot_santa(instructions):
    x_santa = 0
    y_santa = 0

    x_robot = 0
    y_robot = 0

    houses = {(x_santa, y_santa), (x_robot, y_robot)}

    for index, instruction in enumerate(instructions):
        if index % 2 == 0:
            if instruction == '>':
                x_santa += 1
            if instruction == '<':
                x_santa -= 1
            if instruction == '^':
                y_santa += 1
            if instruction == 'v':
                y_santa -= 1

            house = (x_santa, y_santa)

            houses.add(house)
        else:
            if instruction == '>':
                x_robot += 1
            if instruction == '<':
                x_robot -= 1
            if instruction == '^':
                y_robot += 1
            if instruction == 'v':
                y_robot -= 1

            house = (x_robot, y_robot)

            houses.add(house)

    return houses


def solve():
    instructions = read_and_parse_file('input.txt')

    houses = find_visited_houses(instructions)

    print(f'Number of visited houses is {len(houses)}')

    houses = find_visited_houses_with_robot_santa(instructions)

    print(f'Number of visited houses together with Robot Santa is {len(houses)}')


solve()
