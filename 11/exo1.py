# Day 11 Part I of advent of code calendar


data = []

def all_equal(line, char):
    for c in line:
        if c != char:
            return False
    return True

def get_column(j):
    column = []
    for line in data:
        column.append(line[j])
    return column

def print_map():
    for line in data:
        print(*list(line))

with open("11/input.txt", "r") as file:
    for line in file:
        data.append([c for c in line.strip()])
        if all_equal(line.strip(), "."):
            data.append([c for c in line.strip()])
print_map()
for col in range(len(data[0])):
    column = get_column(col)
    if all_equal(column, "."):
        for line in data:
            line.insert(col, ".")

print_map()