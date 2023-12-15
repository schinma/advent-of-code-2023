# Day 15 Part I of advent of code calendar

steps = []


def hash_algo(string):
    value = 0
    for c in string:
        value += ord(c)
        value = value * 17
        value = value % 256
    return value


with open("15/input.txt") as file:
    for line in file:
        steps.extend(line.strip().split(","))

print(sum(map(hash_algo, steps)))
