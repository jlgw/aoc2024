from functools import cache
import math

@cache
def blink_one(stone, times):
    if times == 1:
        if stone == 0:
            return 1
        elif math.floor(math.log10(stone)) % 2 == 1:
            return 2
        else:
            return 1
    else:
        if stone == 0:
            return blink_one(1, times - 1)
        elif math.floor(math.log10(stone)) % 2 == 1:
            st = str(stone)
            fst = int(st[: len(st) // 2])
            snd = int(st[len(st) // 2 :])
            return blink_one(fst, times - 1) + blink_one(snd, times - 1)
        else:
            return blink_one(stone * 2024, times - 1)


# file = "example.txt"
# file = "example2.txt"
file = "input.txt"
line = open(file).read().splitlines()[0]
parsed_line = [int(k) for k in line.split()]

current = parsed_line
print(sum([blink_one(c, 75) for c in parsed_line]))
