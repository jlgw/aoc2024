from collections import defaultdict

up = (-1, 0)
down = (1, 0)
right = (0, 1)
left = (0, -1)

downleft = (1, -1)
downright = (1, 1)
upleft = (-1, -1)
upright = (-1, 1)


def add_tuple(a, b):
    return (a[0] + b[0], a[1] + b[1])


def calc_sides(coordinate_set):
    sm = 0
    for s in coordinate_set:
        sm += calc_side(coordinate_set, s)
    return sm


def calc_side(coordinate_set, coordinates):
    sm = 0
    if (
        add_tuple(coordinates, down) not in coordinate_set
        or add_tuple(coordinates, downright) in coordinate_set
    ) and add_tuple(coordinates, right) not in coordinate_set:
        sm += 1
    if (
        add_tuple(coordinates, down) not in coordinate_set
        or add_tuple(coordinates, downleft) in coordinate_set
    ) and add_tuple(coordinates, left) not in coordinate_set:
        sm += 1
    if (
        add_tuple(coordinates, left) not in coordinate_set
        or add_tuple(coordinates, upleft) in coordinate_set
    ) and add_tuple(coordinates, up) not in coordinate_set:
        sm += 1
    if (
        add_tuple(coordinates, left) not in coordinate_set
        or add_tuple(coordinates, downleft) in coordinate_set
    ) and add_tuple(coordinates, down) not in coordinate_set:
        sm += 1
    return sm


def calc_price(coordinate_set):
    return len(coordinate_set) * calc_sides(coordinate_set)


def has_neighbor(coordinate_set, coordinates):
    if (
        add_tuple(coordinates, up) in coordinate_set
        or add_tuple(coordinates, down) in coordinate_set
        or add_tuple(coordinates, left) in coordinate_set
        or add_tuple(coordinates, right) in coordinate_set
    ):
        return True
    return False


def regions(lines):
    regions = defaultdict(lambda: [])
    for i, line in enumerate(lines):
        for j, s in enumerate(line):
            in_set = []
            for k, coordinate_set in enumerate(regions[s]):
                if has_neighbor(coordinate_set, (i, j)):
                    in_set.append(k)
            if len(in_set) == 0:
                regions[s].append({(i, j)})
            elif len(in_set) == 1:
                regions[s][in_set[0]].add((i, j))
            else:
                regions[s][in_set[0]].add((i, j))
                regions[s][in_set[0]] = regions[s][in_set[0]].union(
                    *[regions[s][k] for k in in_set]
                )
                regions[s] = [
                    v for k, v in enumerate(regions[s]) if k not in in_set[1:]
                ]
    return regions


# file = "example.txt"
# file = "example2.txt"
file = "input.txt"
lines = open(file).read().splitlines()

r = regions(lines)
sm = 0

for symbol, region_list in r.items():
    for region in region_list:
        price = calc_price(region)
        print(symbol, price)
        print(calc_sides(region))
        sm += price
print(sm)
