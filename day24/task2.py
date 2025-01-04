import graphviz

operator_symbol = {"AND": "And", "OR": "Or", "XOR": "Xor"}

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
        rules.append([(arg1, arg2), operator, output])
    return (start_values, rules)


def calculate(value1, value2, operator):
    if operator == "AND":
        return value1 and value2
    if operator == "OR":
        return value1 or value2
    if operator == "XOR":
        return value1 ^ value2


start_values, rules = parse_input(lines)


def pad(num):
    if num >= 10:
        return str(num)
    else:
        return "0" + str(num)


def chain(node):
    if node in start_values.keys():
        return node
    else:
        for rule in rules:
            (arg1, arg2), operator, output = rule
            if output == node:
                return (operator, chain(arg1), chain(arg2))


def order_parents(z_test):
    num = int(z_test[1:])
    contrib_set = {f"x{pad(num)}", f"y{pad(num)}"}
    left_parent = list(parents[z_test])[0]
    left_grandparents = parents[left_parent] if left_parent in parents else None
    right_parent = list(parents[z_test])[1]
    right_grandparents = parents[right_parent] if right_parent in parents else None
    if left_grandparents == contrib_set:
        return left_parent, right_parent
    elif right_grandparents == contrib_set:
        return right_parent, left_parent
    else:
        return None, None


def holds(z_low, z_high):
    if parent_operator[z_low] != "XOR":
        return False
    if parent_operator[z_high] != "XOR":
        return False
    left_low, right_low = order_parents(z_low)
    left_high, right_high = order_parents(z_high)

    if left_low in parent_operator and parent_operator[left_low] != "XOR":
        return False
    if left_high in parent_operator and parent_operator[left_high] != "XOR":
        return False
    if (left_low is None and right_low is None) or (
        left_high is None and right_high is None
    ):
        return False
    grandparents_high = list(parents[right_high])
    great_high = parents[grandparents_high[0]], parents[grandparents_high[1]]
    if great_high[0] != parents[z_low] and great_high[1] != parents[z_low]:
        return False
    return True


def express(node):
    if node in start_values.keys():
        return node
    else:
        for rule in rules:
            (arg1, arg2), operator, output = rule
            symbol = operator_symbol[operator]
            if output == node:
                return f"{symbol}({express(arg1)}, {express(arg2)})"


def plot(node, dot=None):
    plotting = False
    if dot is None:
        dot = graphviz.Digraph(node)
        plotting = True
    for rule in rules:
        (arg1, arg2), operator, output = rule
        if output == node:
            dot.edge(arg1, node, label=operator)
            dot.edge(arg2, node, label=operator)
            plot(arg1, dot)
            plot(arg2, dot)
    if plotting:
        dot.render(view=True)


def swap(rules, node1, node2):
    for rule in rules:
        (arg1, _), __, output = rule
        if output == node1:
            rule[2] = node2
        if output == node2:
            rule[2] = node1


# input data specific
swaps = [("vkq", "z11"), ("mmk", "z24"), ("hqh", "z38"), ("pvb", "qdq")]

for pair in swaps:
    swap(rules, *pair)


all_output_nodes = [rule[2] for rule in rules]
z_outputs = [rule[2] for rule in rules if rule[2][0] == "z"]
z_outputs = [rule[2] for rule in rules if rule[2][0] == "z"]

parents = {}
parent_operator = {}
for rule in rules:
    (arg1, arg2), operator, output = rule
    parents[output] = {arg1, arg2}
    parent_operator[output] = operator


for i, z in enumerate(sorted(z_outputs)):
    expr = express(z)
    for k in range(i + 1):
        if f"x{pad(k)}" not in expr:
            print(f"x{pad(k)} not in {z}")
        if f"y{pad(k)}" not in expr:
            print(f"y{pad(k)} not in {z}")
    for k in range(i + 1, len(z_outputs)):
        if f"x{pad(k)}" in expr:
            print(f"x{pad(k)} in {z}")
        if f"y{pad(k)}" in expr:
            print(f"y{pad(k)} in {z}")

ordered_z = sorted(z_outputs)
for i, j in zip(ordered_z, ordered_z[1:]):
    if holds(i, j):
        pass
    else:
        print(i, j)

plot("z11")
