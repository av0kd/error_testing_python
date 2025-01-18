class Guess:
    def shot(self):
        pass

class Palpite(Guess):
    def __init__(self, num, shot):
        self.num = num
        self.sho = shot

    def shot(self):
        hint = 0
        if (self.sho>self.num):
            hint = 1
        elif (self.sho<self.num):
            hint = -1
        else:
            hint = 0
        
        return hint
        