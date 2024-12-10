def read_and_parse_file(file_path):
    with open(file_path, 'r') as file:
        line = file.readline().strip()

    numbers = list(map(int, line))

    return numbers


def chop_into_buckets(numbers):
    buckets = []
    current_bucket = [numbers[0]]

    for num in numbers[1:]:
        if num == current_bucket[-1]:
            current_bucket.append(num)
        else:
            buckets.append(current_bucket)
            current_bucket = [num]

    buckets.append(current_bucket)

    return buckets


def iterate(numbers, rounds):
    if rounds == 0:
        return numbers

    buckets = chop_into_buckets(numbers)

    iteration = []

    for bucket in buckets:
        iteration.extend([len(bucket), bucket[0]])

    return iterate(iteration, rounds - 1)


def solve():
    numbers = read_and_parse_file('input.txt')

    result = iterate(numbers, 40)

    print(f'The length of the result after 40 iterations is {len(result)}')

    result = iterate(numbers, 50)

    print(f'The length of the result after 50 iterations is {len(result)}')


solve()
