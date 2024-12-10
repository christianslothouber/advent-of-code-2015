import re


def read_and_parse_file(file_path):
    sues = [{} for _ in range(500)]

    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r'Sue (\d+): (.*)', line.strip())

            if match:
                sue_number = int(match.group(1))

                properties_part = match.group(2)
                properties = {'name': sue_number}

                for prop in properties_part.split(', '):
                    key, value = prop.split(': ')
                    properties[key] = int(value)

                sues[sue_number - 1] = properties

    return sues


def is_match_stable(sue):
    if 'children' in sue and sue['children'] != 3:
        return False

    if 'cats' in sue and sue['cats'] != 7:
        return False

    if 'samoyeds' in sue and sue['samoyeds'] != 2:
        return False

    if 'pomeranians' in sue and sue['pomeranians'] != 3:
        return False

    if 'akitas' in sue and sue['akitas'] != 0:
        return False

    if 'vizslas' in sue and sue['vizslas'] != 0:
        return False

    if 'goldfish' in sue and sue['goldfish'] != 5:
        return False

    if 'trees' in sue and sue['trees'] != 3:
        return False

    if 'cars' in sue and sue['cars'] != 2:
        return False

    if 'perfumes' in sue and sue['perfumes'] != 1:
        return False

    return True


def is_match_unstable(sue):
    if 'children' in sue and sue['children'] != 3:
        return False

    if 'cats' in sue and sue['cats'] < 7:
        return False

    if 'samoyeds' in sue and sue['samoyeds'] != 2:
        return False

    if 'pomeranians' in sue and sue['pomeranians'] > 3:
        return False

    if 'akitas' in sue and sue['akitas'] != 0:
        return False

    if 'vizslas' in sue and sue['vizslas'] != 0:
        return False

    if 'goldfish' in sue and sue['goldfish'] > 5:
        return False

    if 'trees' in sue and sue['trees'] < 3:
        return False

    if 'cars' in sue and sue['cars'] != 2:
        return False

    if 'perfumes' in sue and sue['perfumes'] != 1:
        return False

    return True


def solve():
    sues = read_and_parse_file('input.txt')

    matching_sues = list(filter(is_match_stable, sues))
    print(f'Sue {matching_sues[0]['name']} gave me the gift')

    matching_sues = list(filter(is_match_unstable, sues))
    print(f'Wait! Sue {matching_sues[0]['name']} gave me the gift')


solve()
