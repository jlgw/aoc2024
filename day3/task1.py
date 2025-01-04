import re

#file = "example.txt"
file = "input.txt"
expr = open(file).read()

mul_expressions = re.findall("mul\\([0-9]{1,3},[0-9]{1,3}\\)", expr)

nums = [[int(k) for k in l[4:-1].split(',')] for l in mul_expressions]

products = [k[0]*k[1] for k in nums]
print(sum(products))
