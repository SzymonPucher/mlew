from card_types.card_base import CardBase

class CardUnique(CardBase):
    def __init__(self, val):
        self.val = val
        self.sig = val % 4 # 0=pik, 1=trefl, 2=karo, 3=kier