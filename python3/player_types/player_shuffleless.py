from player_types.player_base import PlayerBase

class PlayerShuffleless(PlayerBase):
    def insert_cards(self, new_cards):
        self.cards = new_cards + self.cards