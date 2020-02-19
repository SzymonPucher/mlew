from player_types.player_base import PlayerBase

class PlayerInreverse(PlayerBase):
    def insert_cards(self, new_cards):
        self.cards = list(reversed(new_cards)) + self.cards