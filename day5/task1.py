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

sm = 0
for section in sections:
    flag = True
    for i, val in enumerate(section):
        for _, other in enumerate(section[i + 1 :]):
            if val in order[other]:
                flag = False
    if flag:
        sm += section[len(section) // 2]

print(sm)
