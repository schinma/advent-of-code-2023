import math
import re


schematic = []
result = 0

with open("3/input.txt", "r") as file:
    for line in file.readlines():
        schematic.append("." + line.strip() + ".")

gears = {}

def add_potential_gear(i, j, number):
    if gears.get((i,j)): 
        gears[(i, j)].append(number)
    else:
        gears[(i, j)] = [number]


for i, line in enumerate(schematic):
    numbers = re.finditer("\d+", line)
    for number in numbers:
        count = False
        number_span = number.span()
        number = int(number.group())
        if i - 1 >= 0:
            for elem in schematic[i-1][number_span[0]-1:number_span[1]+1]:
                if elem == "*":
                    add_potential_gear(i-1, schematic[i-1].index(elem, number_span[0]-1), number)
        if line[number_span[0]-1] == "*":
            add_potential_gear(i, number_span[0]-1, number)
        if line[number_span[1]] == "*":
            add_potential_gear(i, number_span[1], number)
        if i + 1 < len(schematic):
            for elem in schematic[i+1][number_span[0]-1:number_span[1]+1]:
                if elem == "*":
                    add_potential_gear(i+1, schematic[i+1].index(elem, number_span[0]-1), number)

for gear, numbers in gears.items():
    if len(numbers) > 1:
        result += math.prod(numbers) 


print(result)