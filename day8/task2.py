from collections import defaultdict
import itertools
import math


def add_tuple(a, b):
    return (a[0] + b[0], a[1] + b[1])


def subtract_tuple(a, b):
    return (a[0] - b[0], a[1] - b[1])


def multiply_tuple_scalar(a, b):
    return (a[0] * b, a[1] * b)


def divide_tuple_scalar(a, b):
    return (a[0] // b, a[1] // b)


def multiply_tuple(a, b):
    return (a[0] * b[0], a[1] * b[1])


# file = "example.txt"
file = "input.txt"
lines = open(file).read().splitlines()

antennas = defaultdict(lambda: [])


def antinodes(pt1, pt2, xmin, xmax, ymin, ymax):
    antinodes = []
    step = subtract_tuple(pt1, pt2)
    smallest_step = divide_tuple_scalar(step, math.gcd(step[0], step[1]))
    i = 0
    while True:
        res = add_tuple(pt1, multiply_tuple_scalar(smallest_step, i))
        if contained(res, xmin, xmax, ymin, ymax):
            antinodes.append(res)
            i += 1
        else:
            break
    i = -1
    while True:
        res = add_tuple(pt1, multiply_tuple_scalar(smallest_step, i))
        if contained(res, xmin, xmax, ymin, ymax):
            antinodes.append(res)
            i -= 1
        else:
            break
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
