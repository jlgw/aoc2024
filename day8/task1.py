from collections import defaultdict

import itertools


def add_tuple(a, b):
    return (a[0] + b[0], a[1] + b[1])


def subtract_tuple(a, b):
    return (a[0] - b[0], a[1] - b[1])


def multiply_tuple_scalar(a, b):
    return (a[0] * b, a[1] * b)


def multiply_tuple(a, b):
    return (a[0] * b[0], a[1] * b[1])


# file = "example.txt"
file = "input.txt"
lines = open(file).read().splitlines()

antennas = defaultdict(lambda: [])


def antinodes(pt1, pt2, xmin, xmax, ymin, ymax):
    antinodes = []
    antinode1 = subtract_tuple(multiply_tuple_scalar(pt1, 2), pt2)
    antinode2 = subtract_tuple(multiply_tuple_scalar(pt2, 2), pt1)
    if contained(antinode1, xmin, xmax, ymin, ymax):
        antinodes.append(antinode1)
    if contained(antinode2, xmin, xmax, ymin, ymax):
        antinodes.append(antinode2)
    return antinodes


def contained(pt, xmin, xmax, ymin, ymax):
    return pt[0] in range(xmin, xmax) and pt[1] in range(ymin, ymax)


for i, line in enumerate(lines):
    for j, s in enumerate(line):
        if s != ".":
            antennas[s].append((i, j))

all_antinodes = set()
xmin = 0
ymin = 0
xmax = len(lines[0])
ymax = len(lines)
for k in antennas.keys():
    for pt1, pt2 in itertools.combinations(antennas[k], 2):
        all_antinodes.update(antinodes(pt1, pt2, xmin, xmax, ymin, ymax))

print(len(all_antinodes))
