import math


def blink(stones):
    out = []
    for s in stones:
        if s == 0:
            out.append(1)
        elif math.floor(math.log10(s)) % 2 == 1:
            st = str(s)
            fst = int(st[: len(st) // 2])
            snd = int(st[len(st) // 2 :])
            out.append(fst)
            out.append(snd)
        else:
            out.append(s * 2024)
    return out


# file = "example.txt"
# file = "example2.txt"
file = "input.txt"
line = open(file).read().splitlines()[0]
parsed_line = [int(k) for k in line.split()]

current = parsed_line
for i in range(25):
    print(i, len(current))
    current = blink(current)
print(len(current))
