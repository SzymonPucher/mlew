import math    
            
class CardBase:
    def __init__(self, val):
        self.num = math.ceil(val/4)
        self.sig = val % 4 # 0=pik, 1=trefl, 2=karo, 3=kier

    def __repr__(self):
        return str(self.num)

    def __lt__(self, val):
        return self.num < val

    def __gt__(self, val):
        return self.num > val

    def __eq__(self, val):
        return self.num == val