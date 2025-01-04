import re


def add_tuple(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mult_tuple_scalar(a, b):
    return (a[0] * b, a[1] * b)


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


# file = "example2.txt"
# file = "example.txt"; width = 11; height = 7
file = "input.txt"
width = 101
height = 103
lines = open(file).read().splitlines()

parsed_lines = [parse_line(l) for l in lines]

new_pos = [
    mod_tuple(add_tuple(pos, mult_tuple_scalar(vel, 100)), (width, height))
    for pos, vel in parsed_lines
]

print(calc_quadrants(new_pos, width, height))
