# Day 11 Part I  and II of advent of code calendar
import itertools

EXPANTION_RATE = 1000000
data = []
galaxy_count = 0
galaxies = {}
col_to_expand = []
line_to_expand = []


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
    print()


def calculate_distance(pair):
    elem1, elem2 = pair
    i1, j1 = galaxies[elem1]
    i2, j2 = galaxies[elem2]
    return abs(i2 - i1) + abs(j2 - j1)


def find_coord_expansion(j, list_to_expand):
    for i, col in enumerate(list_to_expand):
        if j < col:
            return j + i * (EXPANTION_RATE - 1)
    return j + len(list_to_expand) * (EXPANTION_RATE - 1)


with open("11/input.txt", "r") as file:
    for line in file:
        data.append([c for c in line.strip()])

for i, line in enumerate(data):
    if all_equal(line, "."):
        line_to_expand.append(i)

for col in range(len(data[0])):
    column = get_column(col)
    if all_equal(column, "."):
        col_to_expand.append(col)

for i, line in enumerate(data):
    for j, elem in enumerate(line):
        if elem == "#":
            data[i][j] = galaxy_count
            galaxies[galaxy_count] = (find_coord_expansion(i, line_to_expand), find_coord_expansion(j, col_to_expand))
            galaxy_count += 1


print(sum(map(calculate_distance, itertools.combinations(galaxies.keys(), 2))))
