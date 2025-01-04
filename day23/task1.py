from collections import defaultdict

test = False
if test:
    file = "example.txt"
    # file = "example2.txt"
else:
    file = "input.txt"

lines = open(file).read().splitlines()

unparsed_connections = [line.split("-") for line in lines]

groups = []

connections = defaultdict(lambda: set())
for connection in unparsed_connections:
    connections[connection[0]].add(connection[1])
    connections[connection[1]].add(connection[0])

groups = []
for connection in connections:
    nodes = list(connections[connection])
    for i, node1 in enumerate(nodes):
        for j in range(i, len(nodes)):
            node2 = nodes[j]
            if node2 in connections[node1]:
                group = {connection, node1, node2}
                for g in groups:
                    if group == g:
                        break
                else:
                    groups.append(group)

relevant_groups = [g for g in groups if len([1 for k in g if k[0] == "t"]) != 0]
print(len(relevant_groups))
