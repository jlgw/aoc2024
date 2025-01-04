import functools

keypad = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "0": (1, 3),
    "A": (2, 3),
}

direction_pad = {
    "^": (1, 0),
    "A": (2, 0),
    "<": (0, 1),
    "v": (1, 1),
    ">": (2, 1),
}

movements = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1),
    "A": (0, 0),
}


def compile_direction_pad(seq):
    dir_pad_reverse = {v: k for k, v in direction_pad.items()}
    current = direction_pad["A"]
    out = ""
    for s in seq:
        current = add_tuple(current, movements[s])
        if s == "A":
            out += dir_pad_reverse[current]
    return out


def move_keypad(current_value, next_value):
    current_position = keypad[current_value]
    next_position = keypad[next_value]
    change = subtract_tuple(next_position, current_position)
    horizontal = -change[0] * "<" if change[0] < 0 else change[0] * ">"
    vertical = -change[1] * "^" if change[1] < 0 else change[1] * "v"
    if current_position[1] == 3 and next_position[0] == 0:
        out = vertical + horizontal
    elif (
        current_position[0] == 0
        and next_position[1] == 3
        or (change[0] < 0 and change[1] < 0)
    ):
        out = horizontal + vertical
    else:
        out = vertical + horizontal
    return out


def move_keypad_all(sequence):
    output = ""
    current = "A"
    for s in sequence:
        local_output = move_keypad(current, s)
        output += local_output + "A"
        current = s
    return output


@functools.cache
def move_direction_pad(current_value, next_value, depth):
    current_position = direction_pad[current_value]
    next_position = direction_pad[next_value]
    change = subtract_tuple(next_position, current_position)
    horizontal = -change[0] * "<" if change[0] < 0 else change[0] * ">"
    vertical = -change[1] * "^" if change[1] < 0 else change[1] * "v"

    if current_position[0] == 0 and next_position[1] == 0:
        out = horizontal + vertical
    elif current_position[1] == 0 and next_position[0] == 0 or change[0] >= 0:
        out = vertical + horizontal
    else:
        out = horizontal + vertical
    out += "A"
    if depth == 1:
        return len(out)
    else:
        return move_direction_pad_all(out, depth - 1)


@functools.cache
def move_direction_pad_all(sequence, depth):
    output = 0
    current = "A"
    for s in sequence:
        local_output = move_direction_pad(current, s, depth)
        output += local_output
        current = s
    return output


def add_tuple(a, b):
    return (a[0] + b[0], a[1] + b[1])


def subtract_tuple(a, b):
    return (a[0] - b[0], a[1] - b[1])


def get_numerical(seq):
    return int(seq[:-1])


test = False
if test:
    file = "example.txt"
    # file = "example2.txt"
else:
    file = "input.txt"


lines = open(file).read().splitlines()

depth = 25
solutions = []

for line in lines:
    seq = move_keypad_all(line)
    seq = move_direction_pad_all(seq, depth)
    solutions.append(seq)

lengths = [s for s in solutions]
numericals = [get_numerical(l) for l in lines]
print(sum([x * y for x, y in zip(numericals, lengths)]))
