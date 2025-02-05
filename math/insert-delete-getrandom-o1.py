class RandomizedSet:

    def __init__(self):
        self.store = []
        self.ind = {}
    def insert(self, val: int) -> bool:
        if val not in self.ind:
            self.ind[val] = len(self.store)
            self.store.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.ind:
            return False
        remove_ind = self.ind[val]
        last_element = self.store[-1]
        last_element_ind = self.ind[last_element]

        if remove_ind != last_element_ind:
            self.store[remove_ind] = last_element
            self.ind[last_element] = remove_ind
        self.store.pop()
        del self.ind[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.store)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()