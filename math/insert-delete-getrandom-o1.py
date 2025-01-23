from random import choice
class RandomizedSet:
    def __init__(self):
        self.store = []
        self.ind = {}

    def insert(self, val):
        if val not in self.store:
            self.store.append(val)
            self.ind[val] = len(self.store) - 1
            return True
        else:
            return False

    def remove(self, val):
        if val in self.store:
            change_ind = len(self.store) - 1
            change_val = self.store[change_ind]

            if change_ind != self.ind[val]:
                self.store[self.ind[val]] = change_val
                self.ind[change_val] = self.ind[val]
            self.store.pop()
            del self.ind[val]
            return True
        else:
            return False
    
    def getRandom(self):
        return random.choice(self.store)
