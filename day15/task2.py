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
                boxes.add((2 * j, i))
            elif s == "@":
                robot_pos = (2 * j, i)
            elif s == "#":
                walls.add((2 * j, i))
                walls.add((2 * j + 1, i))

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
    return (2 * width, height), robot_pos, boxes, walls, direction


def to_move(pos, boxes, walls, direction, width=2):
    to_move_boxes = []
    new_pos = add_tuple(pos, direction)
    new_pos_left = add_tuple(new_pos, left)
    new_pos_right = add_tuple(new_pos, right)
    if new_pos in walls or (width == 2 and new_pos_right in walls):
        return None
    if new_pos in boxes:
        to_move_boxes.append(new_pos)
        new_boxes = boxes.copy()
        new_boxes.remove(new_pos)
        move = to_move(new_pos, new_boxes, walls, direction)
        if move is None:
            return None
        to_move_boxes += move
    if new_pos_left in boxes:
        to_move_boxes.append(new_pos_left)
        new_boxes = boxes.copy()
        new_boxes.remove(new_pos_left)
        move = to_move(new_pos_left, new_boxes, walls, direction)
        if move is None:
            return None
        to_move_boxes += move
    if width == 2 and new_pos_right in boxes:
        to_move_boxes.append(new_pos_right)
        new_boxes = boxes.copy()
        new_boxes.remove(new_pos_right)
        move = to_move(new_pos_right, new_boxes, walls, direction)
        if move is None:
            return None
        to_move_boxes += move
    return to_move_boxes


def move(robot_pos, boxes, walls, direction):
    to_move_boxes = to_move(robot_pos, boxes, walls, direction, 1)
    if to_move_boxes is None:
        return robot_pos
    for moving_box in set(to_move_boxes):
        boxes.remove(moving_box)
    for moving_box in set(to_move_boxes):
        boxes.add(add_tuple(moving_box, direction))
    return add_tuple(robot_pos, direction)


def draw(dim, robot_pos, boxes, walls):
    return "\n".join(
        [
            "".join(
                [
                    "["
                    if (i, j) in boxes
                    else "]"
                    if (i - 1, j) in boxes
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
# file = "example3.txt"
# file = "example.txt"
file = "input.txt"
lines = open(file).read().splitlines()

dim, robot_pos, boxes, walls, direction = parse_game(lines)
print(draw(dim, robot_pos, boxes, walls))
for d in direction:
    robot_pos = move(robot_pos, boxes, walls, d)
print(gps(boxes))
print(draw(dim, robot_pos, boxes, walls))
