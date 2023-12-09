# Day 8 Part I of advent od code calendar

import re
import math
from itertools import cycle

result = 0


with open("8/input.txt", "r") as file:
    directions = file.readline().strip()
    
    nodes_map = {}
    for line in file.readlines():
        matches = re.match(r"(\w{3}) = \((\w{3}), (\w{3})\)", line)
        if matches:
            nodes_map[matches.group(1)] = (matches.group(2), matches.group(3))

steps_number = []

nodes = [node for node in nodes_map.keys() if node[2] == "A"]

for node in nodes:
    steps = 0
    for step in cycle(directions):
        steps += 1
        if step == "L":
            next_node = nodes_map[node][0]
        else:
            next_node = nodes_map[node][1]
        if next_node.endswith("Z"):
            break
        node = next_node
    
    steps_number.append(steps)

print(math.lcm(*steps_number))