up = (0, -1)
down = (0, 1)
right = (1, 0)
left = (-1, 0)


def add_tuple(a, b):
    return (a[0] + b[0], a[1] + b[1])


def parse_game(lines):
    boxes = set()
    walls = set()
    width = len(lines[0])

    robot_pos = None
    for i, line in enumerate(lines):
        if line == "":
            break
        for j, s in enumerate(line):
            if s == "O":
                boxes.add((j, i))
            elif s == "@":
                robot_pos = (j, i)
            elif s == "#":
                walls.add((j, i))

    height = i
    direction = []
    for j in range(i + 1, len(lines)):
        for _, symbol in enumerate(lines[j]):
            if symbol == "v":
                direction.append(down)
            elif symbol == "^":
                direction.append(up)
            elif symbol == "<":
                direction.append(left)
            elif symbol == ">":
                direction.append(right)
    return (width, height), robot_pos, boxes, walls, direction


def contained(dim, point):
    return (
        point[0] > 0
        and point[0] < dim[0] - 1
        and point[1] > 1
        and point[1] < dim[1] - 1
    )


def move(dim, robot_pos, boxes, walls, direction):
    new_pos = add_tuple(robot_pos, direction)
    if new_pos in walls:
        return robot_pos
    if new_pos not in boxes:
        return new_pos
    box_count = 1
    is_moved = True
    end_pos = new_pos
    while True:
        end_pos = add_tuple(end_pos, direction)
        if end_pos in walls:
            is_moved = False
            break
        if end_pos not in boxes:
            break
        box_count += 1
    if not is_moved:
        return robot_pos
    boxes.remove(new_pos)
    boxes.add(end_pos)
    return new_pos


def draw(dim, robot_pos, boxes, walls):
    return "\n".join(
        [
            "".join(
                [
                    "O"
                    if (i, j) in boxes
                    else "#"
                    if (i, j) in walls
                    else "@"
                    if (i, j) == robot_pos
                    else "."
                    for i in range(dim[0])
                ]
            )
            for j in range(dim[1])
        ]
    )


def gps(boxes):
    sm = 0
    for box in boxes:
        sm += box[1] * 100 + box[0]
    return sm


# file = "example2.txt"
# file = "example.txt"
file = "input.txt"
lines = open(file).read().splitlines()

dim, robot_pos, boxes, walls, direction = parse_game(lines)
print(draw(dim, robot_pos, boxes, walls))
for d in direction:
    robot_pos = move(dim, robot_pos, boxes, walls, d)
print(gps(boxes))
