import re
import numpy as np


def contains_diagonal(ls):
    sm = 0
    for i, row in enumerate(ls):
        for k, letter in enumerate(row):
            if letter == "X":
                if i < len(ls) - 3 and k < len(row) - 3:
                    if (
                        ls[i + 1][k + 1] == "M"
                        and ls[i + 2][k + 2] == "A"
                        and ls[i + 3][k + 3] == "S"
                    ):
                        sm += 1
    print("sm", sm)
    return sm


# file = "example.txt"
file = "input.txt"
lines = open(file).read().splitlines()

word_count = 0
word_count += sum([len(re.findall("XMAS", line)) for line in lines])
word_count += contains_diagonal(lines)

lines = ["".join(l) for l in np.transpose([list(l) for l in lines])]
word_count += sum([len(re.findall("XMAS", line)) for line in lines])
lines = ["".join(l) for l in np.transpose([list(l) for l in lines])]

lines = [l[::-1] for l in lines]
word_count += sum([len(re.findall("XMAS", line)) for line in lines])
word_count += contains_diagonal(lines)
lines = [l[::-1] for l in lines]

lines = ["".join(l) for l in np.transpose([list(l) for l in lines])]
lines = [l[::-1] for l in lines]
word_count += sum([len(re.findall("XMAS", line)) for line in lines])
word_count += contains_diagonal(lines)
lines = [l[::-1] for l in lines]
lines = ["".join(l) for l in np.transpose([list(l) for l in lines])]

lines = [l[::-1] for l in lines]
lines = ["".join(l) for l in np.transpose([list(l) for l in lines])]
lines = [l[::-1] for l in lines]
word_count += contains_diagonal(lines)
lines = [l[::-1] for l in lines]
lines = ["".join(l) for l in np.transpose([list(l) for l in lines])]
lines = [l[::-1] for l in lines]

print(word_count)
