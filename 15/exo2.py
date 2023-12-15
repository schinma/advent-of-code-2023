# Day 15 Part II of advent of code calendar
import re
from collections import defaultdict, OrderedDict

steps = []
boxes = defaultdict(lambda: OrderedDict())


def hash_algo(string):
    value = 0
    for c in string:
        value += ord(c)
        value = value * 17
        value = value % 256
    return value


def get_box_focussing_power(item):
    box_number, box = item
    result = 0
    for i, lense in enumerate(box.values(), 1):
        result += (box_number + 1) * i * lense
    return result


with open("15/input.txt") as file:
    for line in file:
        steps.extend(line.strip().split(","))

for step in steps:
    matches = re.search(r"(\w+)(=|-)(\d{0,1})", step)
    if matches:
        label = matches.group(1)
        box_number = hash_algo(label)
        action = matches.group(2)

        if action == "=":
            lens_number = int(matches.group(3))
            boxes[box_number][label] = lens_number
        else:
            if boxes[box_number].get(label):
                del boxes[box_number][label]


print(sum(map(get_box_focussing_power, boxes.items())))
