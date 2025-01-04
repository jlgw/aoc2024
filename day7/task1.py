# file = "example.txt"
file = "input.txt"
lines = open(file).read().splitlines()


def parse(line):
    result, value_st = line.split(":")
    return int(result), [int(k) for k in value_st.split()]


def holds(res, remainder, current=None):
    if current == None:
        current = remainder[0]
        return holds(res, remainder[1:], current)
    if len(remainder) == 0:
        return res == current
    if current > res:
        return False
    next_val = remainder[0]
    new_current_1 = current * next_val
    new_current_2 = current + next_val
    new_remainder = remainder[1:]
    return holds(res, new_remainder, new_current_1) or holds(
        res, new_remainder, new_current_2
    )


parsed_lines = [parse(line) for line in lines]

holding = [p for p, rem in parsed_lines if holds(p, rem)]
print(sum(holding))
