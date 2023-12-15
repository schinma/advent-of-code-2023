# Day 14 Part I of advent of code calendar

platform = []
result = 0


def get_columns(pattern):
    columns = []
    for j in range(len(pattern[0])):
        column = [line[j] for line in pattern]
        columns.append(column)
    return columns


def roll_rock(col, rock_index):
    i = rock_index
    while i != 0 and col[i - 1] == ".":
        col[i - 1] = "O"
        col[i] = "."
        i = i - 1


def tilt_platform():
    columns = get_columns(platform)
    for col in columns:
        for i, elem in enumerate(col):
            if elem == "O":
                if i == 0 or col[i - 1] == "#" or col[i - 1] == "O":
                    continue
                else:
                    roll_rock(col, i)
    return columns


with open("14/input.txt", "r") as file:
    platform = [[elem for elem in line.strip()] for line in file]

tiled_columns = tilt_platform()

for col in tiled_columns:
    for i, elem in enumerate(col):
        if elem == "O":
            result += len(col) - i

print(result)
