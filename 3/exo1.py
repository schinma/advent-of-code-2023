import re


schematic = []
result = 0

with open("3/input.txt", "r") as file:
    for line in file.readlines():
        schematic.append("." + line.strip() + ".")


for i, line in enumerate(schematic):
    numbers = re.finditer("\d+", line)
    for number in numbers:
        count = False
        number_span = number.span()
        if i - 1 >= 0:
            for elem in schematic[i - 1][number_span[0] - 1 : number_span[1] + 1]:
                if elem != ".":
                    count = True
                    break
        if line[number_span[0] - 1] != "." or line[number_span[1]] != ".":
            count = True
        if i + 1 < len(schematic):
            for elem in schematic[i + 1][number_span[0] - 1 : number_span[1] + 1]:
                if elem != ".":
                    count = True
                    break
        if count:
            result += int(number.group())

print(result)
