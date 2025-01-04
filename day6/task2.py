from collections import defaultdict


def add_tuple(a, b):
    return (a[0] + b[0], a[1] + b[1])


def rotate(a):
    return (a[1], -a[0])


def has_loop(obstructions, guard_position, maxx, maxy):
    visited = defaultdict(lambda: set())
    guard_direction = (-1, 0)

    while True:
        if guard_direction in visited[guard_position]:
            return True, None
        visited[guard_position].add(guard_direction)
        potential_next = add_tuple(guard_position, guard_direction)
        if not (
            potential_next[0] in range(0, maxy) and potential_next[1] in range(0, maxx)
        ):
            return False, visited.keys()
        if potential_next not in obstructions:
            guard_position = potential_next
        else:
            guard_direction = rotate(guard_direction)


# file = "example.txt"
file = "input.txt"
lines = open(file).read().splitlines()

guard_position = None
obstructions = set()

maxy = len(lines)
maxx = len(lines[0])

for i, line in enumerate(lines):
    for j, symbol in enumerate(line):
        if symbol == "#":
            obstructions.add((i, j))
        if symbol == "^":
            guard_position = (i, j)

positions = 0
_, initial_visits = has_loop(obstructions, guard_position, maxx, maxy)
initial_visits = set(initial_visits)

for (i, j) in initial_visits:
    new_obstructions = obstructions.copy()
    new_obstructions.add((i, j))
    loop, _ = has_loop(new_obstructions, guard_position, maxx, maxy)
    if loop:
        positions += 1
        print(positions)
