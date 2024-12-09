import re


def read_and_parse_file(file_path):
    instructions = []

    pattern = r'(toggle|turn off|turn on) (\d+),(\d+) through (\d+),(\d+)'

    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(pattern, line.strip())
            if match:
                command = match.group(1)
                start_coords = (int(match.group(2)), int(match.group(3)))
                end_coords = (int(match.group(4)), int(match.group(5)))
                instructions.append((command, start_coords, end_coords))

    return instructions


def execute_instruction_digital(instruction, lights):
    command, (x1, y1), (x2, y2) = instruction

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if command == 'toggle':
                lights[x][y] = not lights[x][y]

            if command == 'turn off':
                lights[x][y] = False

            if command == 'turn on':
                lights[x][y] = True


def execute_instruction_analog(instruction, lights):
    command, (x1, y1), (x2, y2) = instruction

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if command == 'toggle':
                lights[x][y] += 2

            if command == 'turn off':
                brightness = lights[x][y]

                if brightness > 0:
                    lights[x][y] -= 1

            if command == 'turn on':
                lights[x][y] += 1


def count_lights(lights):
    return sum(sum(row) for row in lights)


def solve():
    instructions = read_and_parse_file('input.txt')

    lights = [[False for _ in range(1000)] for _ in range(1000)]

    for instruction in instructions:
        execute_instruction_digital(instruction, lights)

    print(f'After following instructions, {count_lights(lights)} lights are lit')

    lights = [[0 for _ in range(1000)] for _ in range(1000)]

    for instruction in instructions:
        execute_instruction_analog(instruction, lights)

    print(f'After following instructions, brightness is {count_lights(lights)}')


solve()
