
cards = {}

with open("4/input.txt") as file:
    for line in file.readlines():
        card_number = int(line.split("|")[0].split(":")[0].split()[1])
        cards[card_number] = cards.get(card_number, 0) + 1
        winning_numbers = [int(n) for n in line.split("|")[0].split(":")[1].split()]
        scratched_numbers = [int(n) for n in line.split("|")[1].split()]
        points = len(set(winning_numbers) & set(scratched_numbers))

        for _ in range(cards.get(card_number, 0)):
            for p in range(card_number + 1, card_number + points + 1):
                cards[p] = cards.get(p, 0) + 1
        
    
result = sum(cards.values())

print(result)