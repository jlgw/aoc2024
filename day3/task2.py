import re

#file = "example_2.txt"
file = "input.txt"
expr = open(file).read()

expressions = re.findall("(mul\\([0-9]{1,3},[0-9]{1,3}\\)|do\\(\\)|don't\\(\\))", expr)

enabled = True
prod = 0
for exp in expressions:
    if exp == 'do()':
        enabled = True
    elif exp == "don't()":
        enabled = False
    else:
        nums = [int(k) for k in exp[4:-1].split(',')]
        if enabled:
            prod += nums[0] * nums[1]

print(prod)
