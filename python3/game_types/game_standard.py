import random
from collections import Counter
from copy import copy

from cards.card_standard import Card
from players.player_standard import Player

class Game:
    def __init__(self, config):
        new_deck_generator = Game.get_deck(len(config.players))
        self.players = [Player(player.name, player.type, next(new_deck_generator)) 
                        for player in config.players]
        self.stats = Counter()

    @staticmethod
    def get_deck(portions=2, shuffled=True):
        # create
        deck = [Card(i) for i in range(5, 57)]
        
        #shuffle
        if shuffled:
            random.shuffle(deck)
        
        # divide
        dividor = len(deck)//portions
        offset = 0
        for _ in range(portions):
            yield deck[dividor * offset:dividor * (offset + 1)]
            offset += 1
    
    def get_cards_from_players(self, num, cards, players):
        active_cards = {}
        for player in players:
                try:    
                    # extracts 2 cards in case of war, 1 during normal battle
                    for _ in range(1 if num == 1 else 2):
                        cards += player.remove_cards(1)
                    active_cards[player] = cards[-1]
                except IndexError:
                    if player in self.players:
                        self.players.remove(player)
        return active_cards

    def get_players_of_max_active_cards(self, active_cards):
        max_players = list()
        max_val = 0
        for key, val in active_cards.items():
            if val > max_val:
                max_val = val
                max_players = [key]
            elif val == max_val:
                max_players.append(key)
        return max_players

    def battle(self):
        active_players = copy(self.players)
        cards_in_battle = []
        num = 1
        while(True):
            self.stats['battle_count'] += 1
            # get cards
            active_cards = self.get_cards_from_players(num, cards_in_battle, active_players)
            
            # covers edge case when all active players run out of cards
            if len(active_cards) == 0:
                active_players = list(filter(lambda x: x.has_cards(), copy(self.players)))
                continue
            
            # get players with highest active card on the table
            active_players = self.get_players_of_max_active_cards(active_cards)
            
            # termination condition
            if len(active_players) == 1:
                active_players[0].insert_cards(cards_in_battle)
                break

            # next war
            num += 1
            self.stats['war_count'] += 1
        if num > 1:
            self.stats['war_length_{}'.format(num-1)] += 1

    def play(self):
        # play a game of War
        while(len(self.players) > 1):
            self.battle()
        
        # stats
        self.stats['{} won'.format(self.players[0].name)] = 1
        return self.stats
