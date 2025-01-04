def add_tuple(a, b):
    return (a[0] + b[0], a[1] + b[1])


up = (-1, 0)
down = (1, 0)
right = (0, 1)
left = (0, -1)


def find_trails(lines, x, y):
    val = lines[y][x]
    trail_endings = set()
    for direction in [up, down, left, right]:
        new_x, new_y = add_tuple((x, y), direction)
        if (
            new_x in range(len(lines[0]))
            and new_y in range(len(lines))
            and lines[new_y][new_x] == val + 1
        ):
            if val == 8:
                trail_endings.add((new_x, new_y))
            else:
                trail_endings.update(find_trails(lines, new_x, new_y))
    return trail_endings


def find_zeroes(lines):
    zeroes = []
    for y, line in enumerate(lines):
        for x, v in enumerate(line):
            if v == 0:
                zeroes.append((x, y))
    return zeroes


# file = "example.txt"
# file = "example2.txt"
file = "input.txt"
lines = open(file).read().splitlines()
converted_lines = [[int(k) for k in line] for line in lines]
zeroes = find_zeroes(converted_lines)
sm = 0
for zero in zeroes:
    print("zero", zero)
    sm += len(find_trails(converted_lines, zero[0], zero[1]))
    print(find_trails(converted_lines, zero[0], zero[1]))
print(sm)
