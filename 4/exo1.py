import math

result = 0

with open("4/input.txt") as file:
    for line in file.readlines():
        winning_numbers = [int(n) for n in line.split("|")[0].split(":")[1].split()]
        scratched_numbers = [int(n) for n in line.split("|")[1].split()]
        points = math.floor(pow(2, len(set(winning_numbers) & set(scratched_numbers)) - 1))
        result += points

print(result)