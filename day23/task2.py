from collections import defaultdict
import functools


test = False
if test:
    file = "example.txt"
    # file = "example2.txt"
else:
    file = "input.txt"

lines = open(file).read().splitlines()

pairs = [line.split("-") for line in lines]


connections = defaultdict(lambda: set())
for connection in pairs:
    connections[connection[0]].add(connection[1])
    connections[connection[1]].add(connection[0])


@functools.cache
def fully_connected_subsets(selected, remainder, min_length=0):
    if len(remainder) == 0:
        return [selected]
    if len(selected) + len(remainder) < min_length:
        return []
    out = []
    for i, k in enumerate(remainder):
        if all([k in connections[s] for s in selected]):
            new_remainder = tuple(
                sorted(
                    [
                        r
                        for j, r in enumerate(remainder)
                        if j != i and (r in connections[k] or r == k)
                    ]
                )
            )
            out += fully_connected_subsets(
                tuple(sorted(list(selected) + [k])),
                new_remainder,
            )
    return out


@functools.cache
def longest_fully_connected_subsets(selected, remainder):
    if len(remainder) == 0:
        return selected
    longest = []
    longest_length = 0
    for i, k in enumerate(remainder):
        if all([k in connections[s] for s in selected]):
            new_remainder = tuple(
                sorted(
                    [
                        r
                        for j, r in enumerate(remainder)
                        if j != i and (r in connections[k] or r == k)
                    ]
                )
            )
            local_longest = longest_fully_connected_subsets(
                tuple(sorted(list(selected) + [k])),
                new_remainder,
            )
            if len(local_longest) > longest_length:
                longest_length = len(local_longest)
                longest = local_longest
    return longest


fully_connected = []
longest = []

for first, second in pairs:
    long_length = len(longest)
    local_connected = [f for f in connections[first] if f in connections[second]]
    arg1 = tuple(sorted([first, second]))
    arg2 = tuple(sorted(local_connected))
    longest_candidate = longest_fully_connected_subsets(arg1, arg2)
    if len(longest_candidate) > len(longest):
        longest = longest_candidate
        print(len(longest), longest)

print(",".join(sorted(longest)))
