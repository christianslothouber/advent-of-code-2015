def count_presents_infinite(n):
    divs = divisors(n)
    presents = sum(map(lambda d: d * 10, divs))

    return presents


def count_presents_50(n):
    divs = divisors(n)
    presents = sum(map(lambda d: d * 11, filter(lambda d: d * 50 >= n, divs)))

    return presents


def divisors(n):
    divs = []

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // i)

    return divs


def solve():
    required = 34_000_000

    calculate_part_1(required)
    calculate_part_2(required)


def calculate_part_2(required):
    house = 1

    while True:
        presents = count_presents_50(house)

        if presents >= required:
            print(f'House {house} gets at least {required} presents when elfs are lazy')
            break

        house += 1


def calculate_part_1(required):
    house = 1

    while True:
        presents = count_presents_infinite(house)

        if presents >= required:
            print(f'House {house} gets at least {required} presents')
            break

        house += 1


solve()
