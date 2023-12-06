result = 1

with open("6/input.txt", "r") as file:
    times = [int(t) for t in file.readline().split()[1:]]
    distances = [int(d) for d in file.readline().split()[1:]]

def calculate_distance(time, time_pressed):
    # v = d/t
    # d =  v * t
    
    return time_pressed * (time - time_pressed)

for time, distance in zip(times, distances):
    calculated_distances = []
    for t in range(time):
        d = calculate_distance(time, t)
        if d > distance:
            calculated_distances.append(d)
    result = result * len(calculated_distances)

print(result)