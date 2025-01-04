from functools import cache


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


@cache
def solutions(pattern):
    solution_count = 0
    if len(pattern) == 0:
        return 1
    for towel in towels:
        if pattern[: len(towel)] == towel:
            new_solutions = solutions(pattern[len(towel) :])
            solution_count += new_solutions
    return solution_count


solvable_count = sum([solutions(pattern) for pattern in patterns])
print(solvable_count)
