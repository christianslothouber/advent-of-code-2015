def read_and_parse_file(file_path):
    with open(file_path, 'r') as file:
        strings = file.readlines()

    return strings


def calculate_sugar(string):
    original_len = len(string)
    base = string.strip('"')
    decoded_len = len(bytes(base, "utf-8").decode('unicode-escape'))

    return original_len - decoded_len


def calculate_encoded_sugar(string):
    original_len = len(string)
    encoded_string = string.replace('\\', '\\\\').replace('"', '\\"')
    encoded_string = '"' + encoded_string + '"'
    encoded_len = len(encoded_string)

    return encoded_len - original_len


def solve():
    strings = read_and_parse_file('input.txt')

    sugar = sum(map(calculate_sugar, strings))

    print(f'Amount of string sugar is {sugar}')

    sugar = sum(map(calculate_encoded_sugar, strings))

    print(f'Amount of string sugar after encoding is {sugar}')


solve()
