import re
from typing import List
from unittest import result

card_order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
hand_types = ["five", "four", "full", "three", "twopairs", "onepair", "highcard"]

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

        jokers = hand_cards.get("J")
        if jokers and jokers != 5:
            del hand_cards["J"]
            max_card = max(hand_cards, key=hand_cards.get)
            hand_cards[max_card] += jokers

        match len(hand_cards):
            case 5:
                return "highcard"
            case 4:
                return "onepair"
            case 3:
                if 3 in hand_cards.values():
                    return "three"
                return "twopairs"
            case 2:
                if 4 in hand_cards.values():
                    return "four"
                return "full"
            case 1:
                return "five"

    def __lt__(self, other):
        if hand_types.index(self.type) == hand_types.index(other.type):
            for card, other_card in zip(self.cards, other.cards):
                if card_order.index(card) == card_order.index(other_card):
                    continue
                return card_order.index(card) < card_order.index(other_card)
        else:
            return hand_types.index(self.type) < hand_types.index(other.type)

    def __eq__(self, other):
        return self.cards == other.cards


with open("7/input.txt", "r") as file:
    for line in file:
        match = re.match("(\w{5}) (\d+)", line)
        hands.append(Hand(match.group(1), int(match.group(2))))

sorted_hands = sorted(hands, reverse=True)

for i, hand in enumerate(sorted_hands, 1):
    result += hand.bet * i

print(result)
