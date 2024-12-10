def read_and_parse_file(file_path):
    *lines, _, molecule = open(file_path).readlines()
    replacements = [line.strip().split(' => ') for line in lines]

    return replacements, molecule


def calculate_distinct_molecules(molecule, replacements):
    generated = set()

    for before, after in replacements:
        for i in range(len(molecule)):
            if molecule[i: i + len(before)] == before:
                generated.add(molecule[: i] + after + molecule[i + len(before):])

    return len(generated)


def calculate_minimal_step_count(molecule, replacements):
    original_replacements = replacements.copy()
    steps = 0
    current_molecule = molecule

    while current_molecule != 'e':
        try:
            replacement = max(replacements, key=lambda x: len(x[1]))
        except ValueError:
            replacements = original_replacements.copy()
            replacement = max(replacements, key=lambda x: len(x[1]))

        before, after = replacement
        new_molecule = current_molecule.replace(after, before, 1)

        if current_molecule == new_molecule:
            replacements.remove(replacement)
        else:
            current_molecule = new_molecule
            steps += 1

    return steps


def solve():
    replacements, molecule = read_and_parse_file('input.txt')

    count = calculate_distinct_molecules(molecule, replacements)
    print(f'{count} distinct molecules can be created')

    steps = calculate_minimal_step_count(molecule, replacements)
    print(f'Molecule can be created in {steps} steps')


solve()
