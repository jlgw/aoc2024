import re


test = False
if test:
    file = "example.txt"
    # file = "example2.txt"
else:
    file = "input.txt"

lines = open(file).read().splitlines()


locks = []
keys = []

i = 0
while i < len(lines):
    top_line = lines[i]
    if re.match("^#+$", top_line):
        type = "lock"
    elif re.match("^\\.+$", top_line):
        type = "key"
    else:
        raise Exception("goofed")
    l = len(top_line) * [-1]
    for k, line in enumerate(lines[i:]):
        if line == "":
            i += k
            break
        for j, s in enumerate(line):
            if s == "#":
                l[j] += 1
    else:
        i += k
    if type == "lock":
        locks.append(l)
    else:
        keys.append(l)
    i += 1


def matches(lock, key):
    for l, k in zip(lock, key):
        if l + k > 5:
            return False
    return True


count = 0
for lock in locks:
    for key in keys:
        if matches(lock, key):
            count += 1
print(count)
