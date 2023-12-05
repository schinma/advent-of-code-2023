
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
locations = []

def get_mapping(source, mapping):
    for source_range, destination in mapping.items():
        if source in source_range:
            return source + destination
    return source

with open("5/input.txt") as file:
    seeds = [int(s) for s in file.readline().split(":")[1].split()]
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

for seed in seeds:
    value = seed
    for m in maps:
        value = get_mapping(value, m)
    
    locations.append(value)

result = min(locations)
print(result)
