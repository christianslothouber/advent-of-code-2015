def read_and_parse_file(file_path):
    with open(file_path, 'r') as file:
        strings = file.readlines()

    return strings


def is_nice_string(string):
    vowels = 'aeiou'
    illegal = ['ab', 'cd', 'pq', 'xy']

    vowel_counter = 0
    contains_double = False
    contains_illegal = all(sub not in string for sub in illegal)

    for c in string:
        if c in vowels:
            vowel_counter += 1

        if not contains_double:
            contains_double = c + c in string

    return vowel_counter >= 3 and contains_double and contains_illegal


def is_real_nice_string(string):
    if not has_two_pairs(string):
        return False

    if not has_a_sandwich(string):
        return False

    return True


def has_two_pairs(string):
    for i in range(len(string) - 2):
        if string[i: i + 2] in string[i + 2:]:
            return True

    return False


def has_a_sandwich(string):
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            return True

    return False


def solve():
    strings = read_and_parse_file('input.txt')

    nice_strings = list(filter(is_nice_string, strings))

    print(f'The number of nice strings is {len(nice_strings)}')

    real_nice_strings = list(filter(is_real_nice_string, strings))

    print(f'The number of really nice strings is {len(real_nice_strings)}')


solve()
