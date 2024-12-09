import hashlib


def read_and_parse_file(file_path):
    with open(file_path, 'r') as file:
        key = file.read()

    return key


def solve():
    key = read_and_parse_file('input.txt')

    for i in range(10_000_000):
        string = key + str(i)
        hash = hashlib.md5(str(string).encode('utf-8')).hexdigest()

        if hash.startswith('00000'):
            print(f'Lowest integer with hash with 5 leading zeroes is {i}')
            break

    for i in range(10_000_000):
        string = key + str(i)
        hash = hashlib.md5(str(string).encode('utf-8')).hexdigest()

        if hash.startswith('000000'):
            print(f'Lowest integer with hash with 6 leading zeroes is {i}')
            break


solve()
