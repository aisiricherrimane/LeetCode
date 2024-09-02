class RandomizedSet:

    def __init__(self):
        self.store = []
        self.index = {}
        
    def insert(self, val: int) -> bool:
        if val not in self.index:
            self.index[val] = len(self.store)
            self.store.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.store:
            return False

        ind = self.index[val]
        last_val = self.store[-1]
        self.index[last_val] = ind
        self.store.insert(last_val, ind)
        self.store.pop()
        del self.index[val]
        return True


        

    def getRandom(self) -> int:
        return random.choice(self.store)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()