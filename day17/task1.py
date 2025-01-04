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


# file = "example.txt"
# file = "example2.txt"
file = "input.txt"
lines = open(file).read().splitlines()
program = parse_program(lines)
state, instructions = program
pointer = 0
output = []
while pointer < len(instructions) - 1:
    opcode, operand = instructions[pointer : pointer + 2]
    pointer = parse_instruction(state, pointer, opcode, operand, output)
print(",".join([str(k) for k in output]))
