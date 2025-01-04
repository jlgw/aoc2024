import re


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
        [int(k) for k in re.match(".*=([0-9]*),.*=([0-9]*)", lines[2]).groups()]
    )
    return (a, b, prize)


def brute_force(game):
    a_multiple = 0
    b_multiple = 100
    a = game[0]
    b = game[1]
    res = game[2]
    while True:
        value = add_tuple(
            mult_tuple_scalar(a, a_multiple), mult_tuple_scalar(b, b_multiple)
        )
        if value == res:
            return (a_multiple, b_multiple)
        elif value[0] > res[0] or value[1] > res[1]:
            b_multiple -= 1
        else:
            a_multiple += 1
        if a_multiple > 100 or b_multiple < 0:
            return None


# file = "example2.txt"
# file = "example.txt"
file = "input.txt"
lines = open(file).read().splitlines()
game_lines = [lines[k : k + 3] for k in range(0, len(lines), 4)]
games = [parse_game(g) for g in game_lines]

sm = 0
for game in games:
    res = brute_force(game)
    if res is not None:
        game_cost = res[0] * 3 + res[1]
        sm += game_cost
print(sm)
