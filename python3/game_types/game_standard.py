import random
from collections import Counter

from cards.card_standard import Card
from players.player_standard import Player

class Game:
    def __init__(self, config):
        cards = Game.get_deck(len(config['players']))
        self.players = [Player(player['name'], player['type'], next(cards)) 
                        for player in config['players']]
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


    def all_players_have_cards(self):
        for p in self.players:
            if not p.has_cards():
                return False
        return True


    def battle(self):
        num = 1
        while(True):
            self.stats['battle_count'] += 1
            # get cards
            try:
                p1_card = self.players[0].cards[num * -1]
            except IndexError:
                self.players[0].empty_deck()
                return
            
            try:
                p2_card = self.players[1].cards[num * -1]
            except IndexError:
                self.players[1].empty_deck()
                return
            
            # compare
            if p1_card > p2_card:
                self.players[0].insert_cards(self.players[1].remove_cards(num) + self.players[0].remove_cards(num))
                break
            if p1_card < p2_card:
                self.players[1].insert_cards(self.players[0].remove_cards(num) + self.players[1].remove_cards(num))
                break
            num += 2
            self.stats['war_count'] += 1
        if num > 1:
            self.stats['war_length_{}'.format(num//2)] += 1

    def play(self):
        while(self.all_players_have_cards()):
            self.battle()
        winner = list(filter(lambda x: x.has_cards(), self.players))[0].name
        self.stats['{} won'.format(winner)] = 1
        return self.stats
