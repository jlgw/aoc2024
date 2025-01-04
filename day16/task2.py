import math

up = (0, -1)
down = (0, 1)
right = (1, 0)
left = (-1, 0)

directions = [up, down, left, right]


def rotate_counterclockwise(direction):
    return (direction[1], -direction[0])


def rotate_clockwise(direction):
    return (-direction[1], direction[0])


def add_tuple(a, b):
    return (a[0] + b[0], a[1] + b[1])


class Node:
    def __init__(self, coordinates, direction, sources, score=None):
        self.coordinates = coordinates
        self.direction = direction
        self.sources = sources
        if score is None:
            score = math.inf
        else:
            self.score = score


def parse_game(lines):
    walls = set()
    end = None
    start = None
    for i, line in enumerate(lines):
        for j, s in enumerate(line):
            if s == "#":
                walls.add((j, i))
            if s == "E":
                end = (j, i)
            if s == "S":
                start = (j, i)
    return walls, start, end


# file = "example.txt"
# file = "example2.txt"
file = "input.txt"
lines = open(file).read().splitlines()
game = parse_game(lines)
walls = game[0]
start = game[1]
end = game[2]

nodes = {}


for i in range(len(lines)):
    for j in range(len(lines[0])):
        if (j, i) in walls:
            continue
        for direction in directions:
            nodes[(j, i), direction] = Node((j, i), direction, None, math.inf)


nodes[(start, right)] = Node(start, right, None, 0)
unvisited = nodes.copy()
to_visit = [nodes[(start, right)]]

while True:
    updated = False
    to_visit.sort(key=lambda node: -node.score)
    node = to_visit.pop()
    newly_created = False
    position = node.coordinates
    direction = node.direction
    rotations = [
        rotate_clockwise(direction),
        rotate_counterclockwise(direction),
    ]
    rotation_score = node.score + 1000
    for rotation in rotations:
        if (position, rotation) in unvisited and unvisited[
            (position, rotation)
        ].score >= rotation_score:
            if unvisited[(position, rotation)].score == rotation_score:
                unvisited[(position, rotation)].sources.append(node)
            else:
                unvisited[(position, rotation)].sources = [node]
                unvisited[(position, rotation)].score = rotation_score
            updated = True
            if unvisited[(position, rotation)] not in to_visit:
                to_visit.append(unvisited[(position, rotation)])
    new_position = add_tuple(position, direction)
    move_score = node.score + 1
    if new_position in walls:
        pass
    elif (new_position, direction) in unvisited and unvisited[
        (new_position, direction)
    ].score >= move_score:
        if unvisited[(new_position, direction)].score == move_score:
            unvisited[(new_position, direction)].sources.append(node)
        else:
            unvisited[(new_position, direction)].score = move_score
            unvisited[(new_position, direction)].sources = [node]
        if unvisited[(new_position, direction)] not in to_visit:
            to_visit.append(unvisited[(new_position, direction)])
        updated = True
    del unvisited[(node.coordinates, node.direction)]
    if len(to_visit) == 0:
        break


end_tiles = [nodes[end, direction] for direction in directions]
end_scores = [node.score for node in end_tiles]
min_score = min(end_scores)
min_tile = end_tiles[end_scores.index(min_score)]
current = min_tile
end_path = [current]
optimals = {min_tile}
old_optimals = [min_tile]
while True:
    next_optimals = []
    for optimal in old_optimals:
        if optimal.sources is None:
            continue
        for source in optimal.sources:
            if source not in optimals:
                next_optimals.append(source)
                optimals.add(source)
    if len(next_optimals) == 0:
        break
    old_optimals = next_optimals

optimal_positions = set([optimal.coordinates for optimal in optimals])
print(len(optimal_positions))

path = end_path[::-1]
print(min_score)
