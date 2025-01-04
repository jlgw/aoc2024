import re
import math


def add_tuple(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mult_tuple_scalar(a, b):
    return (a[0] * b, a[1] * b)


def parse_game(lines):
    a = tuple(
        [int(k) for k in re.match(".*\\+([0-9]*),.*\\+([0-9]*)", lines[0]).groups()]
    )
    b = tuple(
        [int(k) for k in re.match(".*\\+([0-9]*),.*\\+([0-9]*)", lines[1]).groups()]
    )
    prize = tuple(
        [
            int(k) + 10000000000000
            for k in re.match(".*=([0-9]*),.*=([0-9]*)", lines[2]).groups()
        ]
    )
    return (a, b, prize)


def calc_ang(vec):
    return vec[0] / vec[1]


def solve_numerical(a, b, c):
    ang_c = calc_ang(c)
    ang_a = calc_ang(a)
    ang_b = calc_ang(b)
    rev = False
    if ang_a > ang_c and ang_b > ang_c:
        return None
    if ang_a < ang_c and ang_b < ang_c:
        return None
    if ang_a > ang_c and ang_b < ang_c:
        a, b = b, a
        rev = True

    epsilon = 1
    b_mult = 0
    factor = 1
    div_loop = 0
    while epsilon > 0.000000000001:
        div_loop += 1
        res = add_tuple(a, mult_tuple_scalar(b, b_mult + factor))
        res_ang = calc_ang(res)
        if res_ang > ang_c:
            factor /= 2
        else:
            b_mult += factor
        epsilon = abs(res_ang - ang_c)
    return 1 / b_mult if rev else b_mult


def solve_approx(a, b, c):
    factor = solve_numerical(a, b, c)
    if factor is None:
        return None
    base = add_tuple(a, mult_tuple_scalar(b, factor))
    multiple = c[0] / base[0]
    return (round(multiple), round(multiple * factor))


def solve_exact(a, b, c):
    sol = solve_approx(a, b, c)
    if sol is None:
        return None
    a_mult_low, b_mult_low = sol
    a_mult_high, b_mult_high = sol
    loops = 100000
    for _ in range(loops):
        res_high = add_tuple(
            mult_tuple_scalar(a, a_mult_high), mult_tuple_scalar(b, b_mult_high)
        )
        if res_high == c:
            return a_mult_high, b_mult_high
        if res_high[0] > c[0] or res_high[1] > c[1]:
            a_mult_high -= 1
        else:
            b_mult_high += 1

        res_low = add_tuple(
            mult_tuple_scalar(a, a_mult_low), mult_tuple_scalar(b, b_mult_low)
        )
        if res_low == c:
            return a_mult_low, b_mult_low
        if res_low[0] > c[0] or res_low[1] > c[1]:
            b_mult_low -= 1
        else:
            a_mult_low += 1
    return None


def diophantine(a, b, c):
    gcd = math.gcd(a, b)
    if c % gcd != 0:
        return None
    u = a / gcd
    v = b / gcd
    return u, v


# file = "example2.txt"
# file = "example.txt"
file = "input.txt"
lines = open(file).read().splitlines()
game_lines = [lines[k : k + 3] for k in range(0, len(lines), 4)]
games = [parse_game(g) for g in game_lines]

sm = 0
for game in games:
    res = solve_exact(*game)
    if res is not None:
        game_cost = res[0] * 3 + res[1]
        sm += game_cost
print(sm)
