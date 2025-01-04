import sys

sys.setrecursionlimit(10000)


def calc_secret(secret, n=1):
    secret_64 = 64 * secret
    secret = (secret ^ secret_64) % 16777216
    secret_32 = secret // 32
    secret = (secret ^ secret_32) % 16777216
    secret_2028 = secret * 2048
    secret = (secret ^ secret_2028) % 16777216
    if n > 1:
        return calc_secret(secret, n - 1)
    return secret


test = False
if test:
    file = "example.txt"
    # file = "example2.txt"
else:
    file = "input.txt"

lines = open(file).read().splitlines()

values = [int(line) for line in lines]
results = [calc_secret(value, 2000) for value in values]
print(sum(results))
