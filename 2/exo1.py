
from unittest import result


cubes = {"red": 12, "blue": 14, "green": 13}

with open("2/input.txt", "r") as file:
    results = 0  
    for line in file.readlines():
        game_number = int(line.split(":")[0].split()[1])
        sets = line.split(":")[1].split(";")
        possible = True
        for s in sets:
            colors = s.split(",")
            for c in colors:
                if cubes[c.split()[1]] < int(c.split()[0]):
                    possible = False
                    break
            if not possible:
                break
        if possible:
            results += game_number

print(results)
        
                    
