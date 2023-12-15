# Day 13 Part I of advent of code calendar

from unittest import result


patterns = []
result = 0


def get_columns(pattern):
    columns = []
    for j in range(len(pattern[0])):
        column = [line[j] for line in pattern]
        columns.append(column)
    return columns


def check_lines(pattern, line_index):
    r1 = iter(range(line_index, -1, -1))
    r2 = iter(range(line_index + 1, len(pattern)))
    while True:
        try:
            i1 = next(r1)
            i2 = next(r2)
            if pattern[i1] != pattern[i2]:
                return False
        except StopIteration:
            return True


def get_reflect_index(pattern):
    for i, line in enumerate(pattern[:-1]):
        if line == pattern[i + 1]:
            if check_lines(pattern, i):
                return i + 1


with open("13/input.txt") as file:
    pattern = []
    for line in file.readlines():
        if line != "\n":
            pattern.append(line.strip())
        else:
            patterns.append(pattern)
            pattern = []
    patterns.append(pattern)

for i, pattern in enumerate(patterns, 1):
    reflect_index = get_reflect_index(pattern)
    if reflect_index:
        result += 100 * reflect_index
        print(f"horizontal: {i}")
    else:
        columns = get_columns(pattern)
        reflect_index = get_reflect_index(columns)
        if reflect_index:
            result += reflect_index
            print(f"vertical: {i}")

print(result)
