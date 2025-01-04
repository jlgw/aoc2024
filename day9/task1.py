def expand(l):
    position_to_id = []
    empty_positions = []
    file = True
    id_number = 0
    pos = 0
    for v in l:
        if file:
            for _ in range(v):
                position_to_id.append(id_number)
                pos += 1
            id_number += 1
        else:
            for _ in range(v):
                position_to_id.append(None)
                empty_positions.append(pos)
                pos += 1
        file = not file
    return position_to_id, empty_positions


def fill(line, empties):
    inv_ind = len(line) - 1
    for _, pos in enumerate(empties):
        while line[inv_ind] == None:
            inv_ind -= 1
        if inv_ind < pos:
            break
        line[pos] = line[inv_ind]
        line[inv_ind] = None
        inv_ind -= 1
    return line[: line.index(None)]


def calc(l):
    sm = 0
    for i, v in enumerate(l):
        sm += i * v
    return sm


# file = "example.txt"
file = "input.txt"
line = open(file).read().splitlines()[0]
converted_line = [int(k) for k in line]
l, e = expand(converted_line)
filled = fill(l, e)
print(calc(filled))
