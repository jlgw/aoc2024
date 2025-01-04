test = False
if test:
    # file = "example.txt"
    file = "example2.txt"
else:
    file = "input.txt"
lines = open(file).read().splitlines()


def parse_input(lines):
    start_values = {}
    i = 0
    for i, line in enumerate(lines):
        if line == "":
            break
        key, value = line.split(": ")
        start_values[key] = int(value)

    rules = []
    for line in lines[i + 1 :]:
        expression, output = line.split(" -> ")
        arg1, operator, arg2 = expression.split(" ")
        rules.append(((arg1, arg2), operator, output))
    return (start_values, rules)


def calculate(value1, value2, operator):
    if operator == "AND":
        return value1 and value2
    if operator == "OR":
        return value1 or value2
    if operator == "XOR":
        return value1 ^ value2


start_values, rules = parse_input(lines)
all_output_nodes = [rule[2] for rule in rules]
z_outputs = [rule[2] for rule in rules if rule[2][0] == "z"]
unset_z = set(z_outputs)
values = start_values.copy()
for output in all_output_nodes:
    if output not in values:
        values[output] = None

unapplied_rules = rules.copy()

while len(unset_z) > 0:
    for i, rule in enumerate(unapplied_rules):
        (arg1, arg2), operator, output = rule
        value1, value2 = values[arg1], values[arg2]
        if value1 is not None and value2 is not None:
            new_value = calculate(value1, value2, operator)
            values[output] = new_value
            unapplied_rules.pop(i)
            if output[0] == "z":
                unset_z.remove(output)
            break
print("\n".join([str(z_key) + ": " + str(values[z_key]) for z_key in z_outputs]))
print([values[z_key] for z_key in sorted(z_outputs)])
print(sum([2**i * values[z_key] for i, z_key in enumerate(sorted(z_outputs))]))
