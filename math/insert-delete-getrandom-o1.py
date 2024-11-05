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
        if val not in self.index:
            return False
        
        last_element = self.store[-1]
        last_element_ind = len(self.store) - 1
        val_ind = self.index[val]

        if val_ind != last_element_ind:
            self.store[val_ind] = last_element
            self.index[last_element] = val_ind

        self.store.pop()
        del self.index[val]
        return True

    def getRandom(self) -> int:
        return choice(self.store)
         
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()