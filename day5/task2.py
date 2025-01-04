import collections

# file = "example.txt"
file = "input.txt"
first, second = open(file).read().split("\n\n")
ordering_data_raw = first.splitlines()
sections_raw = second.splitlines()

ordering_data = [[int(k) for k in nums.split("|")] for nums in ordering_data_raw]
sections = [[int(k) for k in nums.split(",")] for nums in sections_raw]

order = collections.defaultdict(lambda: [])
for item in ordering_data:
    order[item[0]].append(item[1])


def is_correct(section):
    for i, val in enumerate(section):
        for _, other in enumerate(section[i + 1 :]):
            if val in order[other]:
                return False
    return True


def iterate(section):
    for i, val in enumerate(section):
        for j, other in enumerate(section[i + 1 :]):
            if val in order[other]:
                section[i] = other
                section[i + 1 + j] = val
                return False
    return True


initially_incorrect = list(filter(lambda section: not (is_correct(section)), sections))

while True:
    flag = True
    for section in initially_incorrect:
        if not (iterate(section)):
            flag = False
    if flag:
        break

print(sum(map(lambda section: section[len(section) // 2], initially_incorrect)))
