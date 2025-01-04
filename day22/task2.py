import functools
import sys

sys.setrecursionlimit(10000)


@functools.cache
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


@functools.cache
def indices(tup, val):
    return [i for i, k in enumerate(tup) if k == val]


@functools.cache
def subsequence_index(changes, sequence):
    seqlen = len(sequence)
    results = set()
    to_iterate = indices(changes, sequence[0])
    for i in to_iterate:
        if changes[i : i + seqlen] == sequence:
            results.add(i)
    return results


def subsequence_index2(changes, sequence):
    results = set()
    to_iterate = indices(changes, sequence[0])
    for i in to_iterate:
        if i > len(changes) - 2:
            continue
        if changes[i + 1] == sequence[1]:
            results.add(i)
    return results


def all_prices(mods, changes):
    outp = {}
    for i in range(-9, 10):
        for j in range(-9, 10):
            indices = sorted(subsequence_index2(changes, (i, j)))
            for index in indices:
                if index + 5 > len(mods):
                    continue
                price = mods[index + 4]
                k = changes[index + 2]
                l = changes[index + 3]
                if (i, j, k, l) not in outp:
                    outp[(i, j, k, l)] = price
    return outp


def sequence_index(changes, sequence):
    sub1 = sequence[0:2]
    sub2 = sequence[1:3]
    sub3 = sequence[2:4]

    seq1 = subsequence_index(changes, sub1)
    seq2 = subsequence_index(changes, sub2)
    seq3 = subsequence_index(changes, sub3)
    for i in seq1:
        if i + 1 in seq2 and i + 2 in seq3:
            return i
    return -1


def price(mods, changes, sequence):
    index = sequence_index(changes, sequence)
    if index >= 0:
        return mods[index + 4]
    else:
        return 0


def calc_secret_mod(secret):
    out = [secret % 10]
    for _ in range(2000):
        secret = calc_secret(secret)
        out.append(secret % 10)
    return out


def calc_secret_changes(secret_mod):
    return [y - x for x, y in zip(secret_mod, secret_mod[1:])]


test = False
if test:
    # file = "example.txt"
    file = "example2.txt"
else:
    file = "input.txt"


lines = open(file).read().splitlines()

values = [int(line) for line in lines]
mods = [tuple(calc_secret_mod(secret)) for secret in values]
changes = [tuple(calc_secret_changes(mod)) for mod in mods]
all_price_map = []
for i, _ in enumerate(mods):
    print(i)
    all_price_map.append(all_prices(mods[i], changes[i]))

all_key = [set(m.keys()) for m in all_price_map]

all_keys = set()
for i, k in enumerate(all_key):
    print(i)
    all_keys.update(k)

bananas = 0
tup = None
v = {}
for key in all_keys:
    sm = sum([mapper[key] if key in mapper else 0 for mapper in all_price_map])
    v[key] = sm
    if sm > bananas:
        bananas = sm
        tup = key
        print(key, " - ", sm)
