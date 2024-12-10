def parse_reindeer(line):
    parts = line.split(' ')

    name = parts[0]
    speed = int(parts[3])
    distance = 0
    move_time = int(parts[6])
    move_timer = 0
    rest_time = int(parts[13])
    rest_timer = 0
    score = 0

    return [name, speed, distance, move_time, move_timer, rest_time, rest_timer, score]


def read_and_parse_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    reindeer = list(map(parse_reindeer, lines))

    return reindeer


def run(reindeer, seconds):
    for i in range(seconds):
        for r in reindeer:
            if r[4] == r[3]:  # reindeer is tired
                r[4] = 0  # reset move timer
                r[6] = r[5]  # set rest timer

            if r[6] > 0:  # reindeer is resting
                r[6] -= 1  # rest 1 second
            else:
                r[2] += r[1]  # move reindeer
                r[4] += 1  # increase reindeer move timer

        max_distance = get_max_distance(reindeer)

        for r in reindeer:
            if r[2] == max_distance:  # reindeer distance is max distance
                r[7] += 1  # increase reindeer score


def get_max_distance(reindeer):
    max_distance = max(map(lambda r: r[2], reindeer))

    return max_distance


def get_max_score(reindeer):
    max_distance = max(map(lambda r: r[7], reindeer))

    return max_distance


def solve():
    reindeer = read_and_parse_file('input.txt')

    run(reindeer, 2503)

    max_distance = get_max_distance(reindeer)
    max_score = get_max_score(reindeer)

    print(f'Max traveled distance is {max_distance}')
    print(f'Max score is {max_score}')


solve()
