
# There must some ways to optimize this because it took like 4h to run lol

import re
from unittest import result

seed_to_soil = {}
soil_to_fertilizer = {}
fertilizer_to_water = {}
water_to_light = {}
light_to_temperature = {}
temperature_to_humidity = {}
humidity_to_location = {}
maps = []
result = None

def get_mapping(source, mapping):
    for source_range, destination in mapping.items():
        if source in source_range:
            return source + destination
    return source

def get_seeds(line):
    seeds = []
    matches = re.findall(r"(\d+ \d+)", line)
    for match in matches:
        start = int(match.split()[0])
        rang = int(match.split()[1])
        seeds.append(range(start, start+rang))
    return seeds



with open("5/input.txt") as file:
    seeds_range = get_seeds(file.readline())
    last_map = ""
    for line in file.readlines():
        if line == '\n':
            continue
        
        match = re.search(r"([a-z-]+) map:", line)
        if match:
            last_map = match.group(1).replace("-", "_")
            maps.append(globals()[last_map])
        else:
            destination, source, range_ = [int(n) for n in line.split()]
            current_map = globals()[last_map]
            current_map[range(source, source + range_)] = destination - source

for r in seeds_range:
    print(r)
    for seed in r:
        value = seed
        for m in maps:
            value = get_mapping(value, m)
        
        if result is None or value < result :
            result = value

print(result)
