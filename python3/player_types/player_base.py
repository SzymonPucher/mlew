from functools import reduce
import random

class PlayerBase:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
    
    def has_cards(self):
        return True if len(self.cards) > 0 else False

    def empty_deck(self):
        self.cards.clear()

    def insert_cards(self, new_cards):
        random.shuffle(new_cards)
        self.cards = new_cards + self.cards
    
    def remove_cards(self, number):
        return [self.cards.pop() for i in range(number)]
