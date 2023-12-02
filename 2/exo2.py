
import math


with open("2/input.txt", "r") as file:
    results = 0  
    for line in file.readlines():
        cubes = {"red": 0, "blue": 0, "green": 0}
        sets = line.split(":")[1].split(";")
        for s in sets:
            colors = s.split(",")
            for c in colors:
                k = c.split()[1]
                n = int(c.split()[0])
                if cubes[k] < n:
                    cubes[k] = n
        results += math.prod(cubes.values())


print(results)
        
                    
