#file = "example.txt"
file = "input.txt"
lines = open(file).read().splitlines()

numbers = [l.split() for l in lines]

first = [int(l[0]) for l in numbers]
second = [int(l[1]) for l in numbers]

first_s = sorted(first)
second_s = sorted(second)

dist = sum([abs(a-b) for a,b in zip(first_s, second_s)])
print(dist)
