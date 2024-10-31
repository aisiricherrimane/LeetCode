class RandomizedSet:

    def __init__(self):
        self.store = []
        self.ind = {}
        
    def insert(self, val: int) -> bool:
        if val not in self.ind:
            self.store.append(val)
            self.ind[val] = (len(self.store) - 1)
            return True
        else:
            return False
    def remove(self, val: int) -> bool:
        if val not in self.ind:
            return False
        last_element = self.store[-1]
        ind = self.ind[val]
        self.store[ind] = last_element
        self.ind[last_element] = ind
        
        self.store.pop()
        del self.ind[val]
        return True
        
    def getRandom(self) -> int:
        return choice(self.store)
       

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()