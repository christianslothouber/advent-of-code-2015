from string import ascii_lowercase
from itertools import groupby


def read_and_parse_file(file_path):
    with open(file_path, 'r') as file:
        password = file.read().strip()

    return password


def rotate_password(password):
    password = increment_password(password)

    while not is_valid_password(password):
        password = increment_password(password)

    return password


def increment_password(password):
    index = len(password) - 1

    while index > 0:
        cell = password[index]

        if cell == 'z':
            password = password[:index] + 'a' + password[index + 1:]
            index -= 1
        else:
            incremented_cell = chr(ord(cell) + 1)
            password = password[:index] + incremented_cell + password[index + 1:]
            index = 0

    return password


def is_valid_password(password):
    if len(set('iol') & set(password)) > 0:
        return False

    if not any([ascii_lowercase[n: n + 3] in password for n in range(24)]):
        return False

    if sum([2 if len(list(y)) >= 4 else 1 for x, y in groupby(password) if len(list(y)) >= 2]) < 2:
        return False

    return True


def solve():
    password = read_and_parse_file('input.txt')

    new_password = rotate_password(password)

    print(f'The new password is {new_password}')

    ultra_new_password = rotate_password(new_password)

    print(f'The ultra new password is {ultra_new_password}')


solve()
