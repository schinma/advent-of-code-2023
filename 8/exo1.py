# Day 8 Part I of advent od code calendar

import re
from itertools import cycle

result = 0


with open("8/input.txt", "r") as file:
    steps = file.readline().strip()
    
    nodes = {}
    for line in file.readlines():
        matches = re.match(r"(\w{3}) = \((\w{3}), (\w{3})\)", line)
        if matches:
            nodes[matches.group(1)] = (matches.group(2), matches.group(3))

node = nodes["AAA"]

for step in cycle(steps):
    result += 1
    if step == "L":
        next_node = node[0]
    else:
        next_node = node[1]
    if next_node == "ZZZ":
        break
    node = nodes[next_node]

print(result)