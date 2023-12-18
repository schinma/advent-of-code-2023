# Day 18 Part I of advent of code calendar

ground = {}

with open("18/input.txt", "r") as file:
    plan = [
        (direction, int(distance), color)
        for direction, distance, color in [line.strip().split() for line in file.readlines()]
    ]

first_coord = (0, 0)

for direction in plan:
    if direction[0] == "R":
        for i in range(direction[1]):
            first_coord = (first_coord[0] + 1, first_coord[1])
            ground[first_coord] = direction[2]
    elif direction[0] == "L":
        for i in range(direction[1]):
            first_coord = (first_coord[0] - 1, first_coord[1])
            ground[first_coord] = direction[2]
    elif direction[0] == "U":
        for i in range(direction[1]):
            first_coord = (first_coord[0], first_coord[1] + 1)
            ground[first_coord] = direction[2]
    elif direction[0] == "D":
        for i in range(direction[1]):
            first_coord = (first_coord[0], first_coord[1] - 1)
            ground[first_coord] = direction[2]
