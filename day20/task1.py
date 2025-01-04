import math

up = (0, -1)
down = (0, 1)
right = (1, 0)
left = (-1, 0)

directions = [up, down, left, right]


def add_tuple(a, b):
    return (a[0] + b[0], a[1] + b[1])


upleft = add_tuple(up, left)
upright = add_tuple(up, right)
downleft = add_tuple(down, left)
downright = add_tuple(down, right)


def mult_tuple(a, b):
    return (a[0] * b[0], a[1] * b[1])


def mult_tuple_scalar(a, b):
    return (a[0] * b, a[1] * b)


def mod_tuple(a, b):
    return (a[0] % b[0], a[1] % b[1])


def mod_tuple_scalar(a, b):
    return (a[0] % b, a[1] % b)


test = False
if test:
    file = "example.txt"
    # file = "example2.txt"
else:
    file = "input.txt"


def parse_lines(lines):
    start, end = None, None
    walls = set()
    for j, line in enumerate(lines):
        for i, s in enumerate(line):
            if s == "#":
                walls.add((i, j))
            elif s == "S":
                start = (i, j)
            elif s == "E":
                end = (i, j)
    return walls, start, end


def dijkstra(start, nodes):
    unvisited = {}
    visited = {}
    for node in nodes:
        unvisited[node] = math.inf
    preliminaries = [start]
    unvisited[start] = 0
    while True:
        if len(preliminaries) == 0:
            break
        preliminaries.sort(key=lambda v: -unvisited[v])
        selected = preliminaries.pop()
        new_score = unvisited[selected] + 1
        for direction in [up, down, left, right]:
            new_node = add_tuple(selected, direction)
            if new_node not in unvisited:
                continue
            if new_score < unvisited[new_node]:
                unvisited[new_node] = new_score
                if new_node not in preliminaries:
                    preliminaries.append(new_node)
        visited[selected] = unvisited[selected]
        del unvisited[selected]
    return visited


def cheat(start_distances, end_distances):
    cheat_scores = {}
    directions = [
        mult_tuple_scalar(up, 2),
        mult_tuple_scalar(down, 2),
        mult_tuple_scalar(left, 2),
        mult_tuple_scalar(right, 2),
        upleft,
        upright,
        downleft,
        downright,
    ]
    for node in start_distances:
        score1 = start_distances[node]
        for direction in directions:
            new_node = add_tuple(node, direction)
            score2 = end_distances[new_node] if new_node in end_distances else math.inf
            new_score = score1 + score2 + 2
            if new_score < math.inf:
                cheat_scores[(node, new_node)] = new_score
    return cheat_scores


lines = open(file).read().splitlines()

walls, start, end = parse_lines(lines)
height, width = len(lines), len(lines[0])
nodes = set()
for i in range(width):
    for j in range(height):
        if (i, j) not in walls:
            nodes.add((i, j))
start_scores = dijkstra(start, nodes)
end_scores = dijkstra(end, nodes)
original_score = end_scores[start]
scores = cheat(start_scores, end_scores)
savings = [original_score - score for score in sorted(scores.values())]
print(len(list(filter(lambda x: x >= 100, savings))))
