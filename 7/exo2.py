import re
from typing import List
from unittest import result

card_order =  ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
hand_types =  ["five", "four", "full", "three", "twopairs", "onepair", "highcard"]

hands = []

result = 0

class Hand:
    def __init__(self, cards: List[str], bet: int) -> None:
        self.cards: List[str] = cards
        self.type: str = self.calculate_type(self.cards)
        self.bet: int = bet

    def calculate_type(self, hand: str):
        hand_cards = {}
        for card in hand:
            hand_cards[card] = hand_cards.get(card, 0) + 1
        
        match len(hand_cards):
            case 5:
                hand_type = "highcard"
            case 4:
                hand_type = "onepair"
            case 3:
                if 3 in hand_cards.values():
                    hand_type = "three"
                else:
                    hand_type = "twopairs"
            case 2:
                if 4 in hand_cards.values():
                    hand_type = "four"
                else:
                    hand_type = "full"
            case 1:
                return "five"
        
        if jokers := hand_cards.get("J"):
            hand_type += jokers
        
        return hand_type

    def __lt__(self, other):
        if hand_types.index(self.type) == hand_types.index(other.type):
            for i in range(5):
                if card_order.index(self.cards[i]) == card_order.index(other.cards[i]):
                    continue
                return card_order.index(self.cards[i]) < card_order.index(other.cards[i])
        else:
            return hand_types.index(self.type) < hand_types.index(other.type)
    
    def __eq__(self, other):
        return self.cards == other.cards
    
    def __repr__(self) -> str:
        return f"Hand({self.cards} {self.type} {self.bet})"
        

with open("7/input.txt", "r") as file:
    for line in file:
        match = re.match("(\w{5}) (\d+)", line)
        hands.append(Hand(match.group(1), int(match.group(2))))

sorted_hands = sorted(hands, reverse=True)

for i, hand in enumerate(sorted_hands, 1):
    result += hand.bet * i

print(result)