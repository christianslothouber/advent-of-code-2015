import re
import json


def read_and_parse_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read().strip()

    return text


def evaluate(data):
    if isinstance(data, int):
        return data

    if isinstance(data, list):
        return sum([evaluate(d) for d in data])

    if isinstance(data, dict):
        if 'red' not in data.values():
            return evaluate(list(data.values()))

    return 0


def solve():
    text = read_and_parse_file('input.txt')

    num_strings = re.findall(r'(?<!\d)-?\d+', text)
    total = sum(map(int, num_strings))

    print(f'The sum of all numbers is {total}')

    deserialized = json.loads(text)
    filtered_total = evaluate(deserialized)

    print(f'After filtering red objects, the sum of all numbers is {filtered_total}')


solve()
