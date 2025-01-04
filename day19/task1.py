def parse_input(lines):
    towels = lines[0].split(", ")
    patterns = lines[2:]
    return towels, patterns


def can_solve(towels, pattern):
    if len(pattern) == 0:
        return True
    for towel in towels:
        if pattern[: len(towel)] == towel:
            if can_solve(towels, pattern[len(towel) :]):
                return True
    return False


test = False
if test:
    file = "example.txt"
    # file = "example2.txt"
else:
    file = "input.txt"


lines = open(file).read().splitlines()
towels, patterns = parse_input(lines)

solvable_count = sum([can_solve(towels, pattern) for pattern in patterns])
print(solvable_count)
