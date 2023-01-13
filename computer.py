from random import randint

class Dice:
    
    def __init__(self):
        self.surface = [1, 2, 3, 4, 5, 6]
        self.current_value = 0
    
    def roll(self):
        random_number = randint(0, 5)
        self.current_value = self.surface(random_number)
        return self.current_value
    
    def is_one(self):
        return self.current_value is 1       
