import math    
            
class CardBase:
    def __init__(self, val):
        self.val = math.ceil(val/4)
        self.sig = val % 4 # 0=pik, 1=trefl, 2=karo, 3=kier

    def __repr__(self):
        return str(self.val)

    def __lt__(self, val):
        return self.val < val

    def __gt__(self, val):
        return self.val > val

    def __eq__(self, val):
        return self.val == val