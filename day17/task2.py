import re


def combo_operand(state, value):
    if value in range(4):
        return value
    if value == 4:
        return state["A"]
    if value == 5:
        return state["B"]
    if value == 6:
        return state["C"]
    return None


def parse_instruction(state, pointer, opcode, operand, output):
    # check if xors actually work
    combo = combo_operand(state, operand)
    if opcode == 0:  # adv
        numerator = state["A"]
        denominator = 2**combo
        state["A"] = numerator // denominator
    if opcode == 1:  # bxl
        state["B"] = state["B"] ^ operand
    if opcode == 2:  # bst
        state["B"] = combo % 8
    if opcode == 3:  # jnz
        if state["A"] == 0:
            pass
        else:
            return operand
    if opcode == 4:  # bxc
        state["B"] = state["B"] ^ state["C"]
    if opcode == 5:  # out
        output.append(combo % 8)
    if opcode == 6:  # bdv
        numerator = state["A"]
        denominator = 2**combo
        state["B"] = numerator // denominator
    if opcode == 7:  # cdv
        numerator = state["A"]
        denominator = 2**combo
        state["C"] = numerator // denominator
    return pointer + 2


def parse_program(lines):
    registers = {}
    for i, line in enumerate(lines):
        if line == "":
            break
        register, unparsed_value = re.match("Register (.): (.*)$", line).groups()
        registers[register] = int(unparsed_value)
    instructions = [int(v) for v in lines[i + 1].split(": ")[1].split(",")]
    return registers, instructions


def submatch(to_test, actual):
    for i, t in enumerate(to_test):
        if actual[i] != t:
            return False
    return True


def next_state(state):
    x = state["A"]
    y = (x % 8) ^ 3
    state["A"] = x // 8
    state["B"] = (y ^ 4) ^ (x // (2**y))
    state["C"] = x // (2**y)
    return state["B"] % 8


file = "example.txt"
# file = "example2.txt"
file = "input.txt"
lines = open(file).read().splitlines()
program = parse_program(lines)
actual_state, instructions = program
st_instructions = ",".join([str(k) for k in instructions])
instruction_l = len(instructions)


def matching_rev(l1, l2):
    sm = 0
    for i, j in zip(l1[::-1], l2[::-1]):
        if i != j:
            return sm
        else:
            sm += 1
    return sm


def test(l):
    state = actual_state.copy()
    state["A"] = l
    output = []
    pointer = 0
    while pointer < len(instructions) - 1:
        opcode, operand = instructions[pointer : pointer + 2]
        pointer = parse_instruction(state, pointer, opcode, operand, output)
    return output


actual = 0
min_x = 0
max_x = 64
found = 0
attempt = 0
while found < 16:
    for i in range(min_x, max_x):
        offset = i - min_x
        output = test(i)
        j = matching_rev(output, instructions)
        if j > found:
            print(j, i, offset, output)
            if i > 0 and j != 16:
                min_x = i * 8
                max_x = min(min_x + 1000, i * 9)
            found = j
            break
print(i)
