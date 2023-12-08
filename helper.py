import os
import sys

def create_folder(day_number):
    os.mkdir(day_number)
    with open(f"{day_number}/exo1.py", "w") as file:
        file.write(f"# Day {day_number} Part I of advent of code calendar")
    
    with open(f"{day_number}/input.txt", "w") as file:
        pass

create_folder(sys.argv[1])