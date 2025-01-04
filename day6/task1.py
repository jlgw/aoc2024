from collections import defaultdict


def add_tuple(a, b):
    return (a[0] + b[0], a[1] + b[1])


def rotate(a):
    return (a[1], -a[0])


# file = "example.txt"
file = "input.txt"
lines = open(file).read().splitlines()

guard_position = None
obstructions = set()

for i, line in enumerate(lines):
    for j, symbol in enumerate(line):
        if symbol == "#":
            obstructions.add((i, j))
        if symbol == "^":
            guard_position = (i, j)

maxy = len(lines)
maxx = len(lines[0])

visited = defaultdict(lambda: set())
guard_direction = (-1, 0)

while True:
    if guard_direction in visited[guard_position]:
        break
    visited[guard_position].add(guard_direction)
    potential_next = add_tuple(guard_position, guard_direction)
    if not (
        potential_next[0] in range(0, maxy) and potential_next[1] in range(0, maxx)
    ):
        break
    if potential_next not in obstructions:
        guard_position = potential_next
    else:
        guard_direction = rotate(guard_direction)

keys = visited.keys()

for k in keys:
    lines[k[0]] = lines[k[0]][: k[1]] + "X" + lines[k[0]][k[1] + 1 :]

print(len(keys))
