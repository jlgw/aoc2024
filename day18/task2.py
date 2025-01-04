import math

up = (0, -1)
down = (0, 1)
right = (1, 0)
left = (-1, 0)


def add_tuple(a, b):
    return (a[0] + b[0], a[1] + b[1])


class Node:
    def __init__(self, coordinates, direction, source, score=None):
        self.coordinates = coordinates
        self.direction = direction
        self.source = source
        if score is None:
            score = math.inf
        else:
            self.score = score


test = False
if test:
    height = 7
    width = 7
    byte_length = 12
    file = "example.txt"
    # file = "example2.txt"
else:
    height = 71
    width = 71
    byte_length = 1024
    file = "input.txt"


def draw(positions, visited=None):
    if visited is None:
        visited = []
    return "\n".join(
        [
            "".join(
                [
                    "#" if (i, j) in positions else "*" if (i, j) in visited else "."
                    for i in range(width)
                ]
            )
            for j in range(height)
        ]
    )


lines = open(file).read().splitlines()


def get_min(key_list, value_dict):
    mv = None
    minimum = math.inf
    for k in key_list:
        if value_dict[k] < minimum:
            mv = k
            minimum = value_dict[k]
    return mv


def dijkstra(unvisited, start, end):
    visited = {}
    unvisited[start] = 0
    preliminaries = [start]
    while True:
        if len(preliminaries) == 0:
            break

        p = get_min(preliminaries, unvisited)
        preliminaries.pop(preliminaries.index(p))
        new_score = unvisited[p] + 1
        all_neighbors = [
            add_tuple(p, direction) for direction in [up, down, left, right]
        ]
        neighbors = list(filter(lambda v: v in unvisited, all_neighbors))
        for n in neighbors:
            if new_score < unvisited[n]:
                unvisited[n] = new_score
                preliminaries.append(n)
        visited[p] = unvisited[p]
        del unvisited[p]
    return visited[end] if end in visited else None


start = (0, 0)
end = (width - 1, height - 1)

all_positions = [(int(line.split(",")[0]), int(line.split(",")[1])) for line in lines]
for bl in range(byte_length + 1950, len(all_positions)):
    positions = all_positions[:bl]
    unvisited = {}
    for j in range(height):
        for i in range(width):
            if (i, j) not in positions:
                unvisited[(i, j)] = math.inf
    res = dijkstra(unvisited, start, end)
    if res is None:
        print(all_positions[bl - 1])
        break
