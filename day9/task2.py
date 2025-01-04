def expand(l):
    position_to_id = {}
    id_to_length = {}
    empty_positions = []
    empty_lengths = {}
    file = True
    id_number = 0
    pos = 0
    for v in l:
        if file:
            position_to_id[pos] = id_number
            pos += v
            id_to_length[id_number] = v
            id_number += 1
        else:
            empty_positions.append(pos)
            empty_lengths[pos] = v
            pos += v
        file = not file
    return position_to_id, id_to_length, empty_positions, empty_lengths


def expand2(position_to_id, id_to_length):
    max_pos = max(position_to_id.keys())
    length = id_to_length[position_to_id[max_pos]]
    total_length = max_pos + length
    out = total_length * ["."]
    for p, i in position_to_id.items():
        length = id_to_length[i]
        for l in range(length):
            out[p + l] = str(i)
    return "".join(out)


def calculate(position_to_id, id_to_length):
    sm = 0
    for k, v in position_to_id.items():
        for i in range(id_to_length[v]):
            sm += (k + i) * v
    return sm


def fill(position_to_id, id_to_length, empty_positions, empty_lengths):
    position_to_id = position_to_id.copy()
    items = sorted(list(position_to_id.items()), key=lambda x: -x[0])
    for k, v in items:
        length = id_to_length[v]
        for j, empty_pos in enumerate(empty_positions):
            empty_length = empty_lengths[empty_pos]
            if empty_pos > k:
                break
            if length > empty_length:
                continue
            del position_to_id[k]
            position_to_id[empty_pos] = v
            if empty_length == length:
                del empty_lengths[empty_pos]
                empty_positions.pop(j)
            else:
                del empty_lengths[empty_pos]
                empty_positions[j] = empty_pos + length
                empty_lengths[empty_positions[j]] = empty_length - length
            break
    return position_to_id


def calc(l):
    sm = 0
    for i, v in enumerate(l):
        sm += i * v
    return sm


# file = "example.txt"
file = "input.txt"
line = open(file).read().splitlines()[0]
converted_line = [int(k) for k in line]
position_to_id, id_to_length, empty_positions, empty_lengths = expand(converted_line)
filled = fill(position_to_id, id_to_length, empty_positions, empty_lengths)
print(calculate(filled, id_to_length))
