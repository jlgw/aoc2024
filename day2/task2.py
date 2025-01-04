# file = "example.txt"
file = "input.txt"
lines = open(file).read().splitlines()


def old_safe(l):
    diff = list(map(lambda x: x[1] - x[0], zip(l, l[1:])))
    if not (all(map(lambda x: x > 0, diff)) or all(map(lambda x: x < 0, diff))):
        return False
    if max(diff) > 3 or min(diff) < -3:
        return False
    return True


# kind of a hack but should work
def safe(l):
    if old_safe(l):
        return True
    for i, _ in enumerate(l):
        new = l[:i] + l[i + 1 :]
        if old_safe(new):
            return True
    return False


numbers = [[int(k) for k in l.split()] for l in lines]
print(sum([safe(num) for num in numbers]))
