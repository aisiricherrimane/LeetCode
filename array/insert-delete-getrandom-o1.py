from random import choice
class RandomizedSet:
    def __init__(self):
        self.store = []

    def insert(self, val):
        if val not in self.store:
            self.store.append(val)
            return True
        else:
            return False

    def remove(self, val):
        if val in self.store:
            self.store.remove(val)
            return True
        else:
            return False
    
    def getRandom(self):
        return random.choice(self.store)
