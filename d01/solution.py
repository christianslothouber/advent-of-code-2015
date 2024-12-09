def read_and_parse_file(file_path):
    with open(file_path, 'r') as file:
        instructions = file.read()

    return instructions


def solve():
    instructions = read_and_parse_file('input.txt')

    floor = 0

    for instruction in instructions:
        if instruction == '(':
            floor += 1
        if instruction == ')':
            floor -= 1

    print(f'Instructions take you to floor {floor}')

    floor = 0

    for index, instruction in enumerate(instructions):
        if instruction == '(':
            floor += 1
        if instruction == ')':
            floor -= 1

        if floor < 0:
            print(f'Instruction {index + 1} take you to the basement')
            break


solve()
