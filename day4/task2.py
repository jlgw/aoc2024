# file = "example.txt"
file = "input.txt"
lines = open(file).read().splitlines()

sm = 0
for i, row in list(enumerate(lines))[1:-1]:
    for j, char in list(enumerate(row))[1:-1]:
        if char != "A":
            continue
        if set([lines[i - 1][j - 1], lines[i + 1][j + 1]]) == {"M", "S"} and set(
            [lines[i + 1][j - 1], lines[i - 1][j + 1]]
        ) == {"M", "S"}:
            sm += 1
print(sm)
