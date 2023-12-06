import math

with open("6/input.txt", "r") as file:
    time = int("".join(file.readline().split()[1:]))
    distance = int("".join(file.readline().split()[1:]))


def calculate_range(t, d):
    # d =  v * t
    # (time_pressed * (time - time_pressed)) > reccord_distance
    # - x^2 + x * time - d > 0
    delta = t**2 - 4 * d
    range_start = math.ceil((-t + math.sqrt(delta)) / (-2))
    range_end = math.floor((-t - math.sqrt(delta)) / (-2))
    return range_end - range_start + 1


results = calculate_range(time, distance)
print(results)
