def read_and_parse_file(file_path):
    grid = []

    with open(file_path, 'r') as file:
        for line in file:
            grid.append([char == '#' for char in line.strip()])

    return grid


def copy_grid(grid):
    return [row[:] for row in grid]


def increment(grid, steps, defect):
    if steps == 0:
        return grid

    new_grid = copy_grid(grid)

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            current_light = grid[x][y]
            neighbour_lights = get_neighbour_lights(grid, (x, y))

            if current_light:
                if neighbour_lights == 2 or neighbour_lights == 3:
                    new_grid[x][y] = True
                else:
                    new_grid[x][y] = False
            else:
                if neighbour_lights == 3:
                    new_grid[x][y] = True
                else:
                    new_grid[x][y] = False

    if defect:
        light_up_corners(new_grid)

    return increment(new_grid, steps - 1, defect)


def get_neighbour_lights(grid, point):
    x, y = point
    lights = 0

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue

            target = (x + dx, y + dy)

            if is_valid_position(grid, target):
                lights += grid[target[0]][target[1]]

    return lights


def is_valid_position(grid, position):
    (x, y) = position

    if x < 0 or x >= len(grid):
        return False
    if y < 0 or y >= len(grid[0]):
        return False

    return True


def count_lights(grid):
    return sum(map(sum, grid))


def light_up_corners(grid):
    grid[0][0] = True
    grid[0][len(grid) - 1] = True
    grid[len(grid) - 1][0] = True
    grid[len(grid) - 1][len(grid[0]) - 1] = True


def solve():
    grid = read_and_parse_file('input.txt')
    steps = 100

    new_grid = increment(grid, steps, False)
    print(f'{count_lights(new_grid)} lights are turned on after {steps} steps')

    light_up_corners(grid)
    new_grid = increment(grid, steps, True)
    print(f'{count_lights(new_grid)} lights are turned on after {steps} steps when defect')


solve()
