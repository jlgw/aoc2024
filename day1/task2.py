#file = "example.txt"
file = "input.txt"
lines = open(file).read().splitlines()

numbers = [l.split() for l in lines]

first = [int(l[0]) for l in numbers]
second = [int(l[1]) for l in numbers]

first_counts = [f*second.count(f) for f in first]
print(sum(first_counts))
