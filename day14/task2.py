import re


def add_tuple(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mod_tuple(a, b):
    return (a[0] % b[0], a[1] % b[1])


def parse_line(line):
    groups = re.match("p=(-?\\d*),(-?\\d*) v=(-?\\d*),(-?\\d*)", line).groups()
    return tuple([int(k) for k in groups[:2]]), tuple([int(k) for k in groups[2:]])


def calc_quadrants(positions, width, height):
    height = height - 1
    width = width - 1
    quad1 = len(
        [
            1
            for position in positions
            if position[0] < width / 2 and position[1] < height / 2
        ]
    )
    quad2 = len(
        [
            1
            for position in positions
            if position[0] > width / 2 and position[1] < height / 2
        ]
    )
    quad3 = len(
        [
            1
            for position in positions
            if position[0] < width / 2 and position[1] > height / 2
        ]
    )
    quad4 = len(
        [
            1
            for position in positions
            if position[0] > width / 2 and position[1] > height / 2
        ]
    )
    return quad1 * quad2 * quad3 * quad4


def plot(positions, width, height):
    return "\n".join(
        [
            "".join(
                [
                    str(positions.count((x, y))) if (x, y) in positions else "."
                    for x in range(width)
                ]
            )
            for y in range(height)
        ]
    )


def cluster(positions):
    x = [pos[0] for pos in positions]
    y = [pos[1] for pos in positions]
    xm = max([x.count(v) for v in set(x)])
    ym = max([y.count(v) for v in set(y)])
    return (xm, ym)


def diagonals(positions):
    right = [pos[0] + pos[1] for pos in positions]
    left = [pos[0] - pos[1] for pos in positions]
    xm = max([right.count(v) for v in set(right)])
    ym = max([left.count(v) for v in set(left)])
    return (xm, ym)


# file = "example2.txt"
# file = "example.txt"; width = 11; height = 7
file = "input.txt"
width = 101
height = 103
lines = open(file).read().splitlines()

parsed_lines = [parse_line(l) for l in lines]

positions = [line[0] for line in parsed_lines]
velocities = [line[1] for line in parsed_lines]

glob_xm = 0
glob_ym = 0
i = 1
while True:
    positions = [
        mod_tuple(add_tuple(positions[j], velocities[j]), (width, height))
        for j, _ in enumerate(positions)
    ]
    xm, ym = diagonals(positions)
    if xm > glob_xm:
        print(i, xm, ym)
        print(plot(positions, width, height))
        glob_xm = xm
    if ym > glob_ym:
        print(plot(positions, width, height))
        glob_ym = ym

    i += 1
    if i % 1000 == 0:
        print(i)
