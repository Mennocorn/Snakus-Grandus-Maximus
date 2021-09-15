import random

class Apple:
    def __init__(self):
        self.x = random.randint(1,2)
        self.y = random.randint(1,2)


    def __int__(self):
        return self.x, self.y