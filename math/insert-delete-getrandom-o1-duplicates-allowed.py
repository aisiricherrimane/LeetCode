class RandomizedCollection:

    def __init__(self):
        self.store = []
        self.ind = defaultdict(list)

    def insert(self, val: int) -> bool:
        self.store.append(val)
        self.ind[val].append(len(self.store) - 1)
        return len(self.ind[val]) == 1
        
    def remove(self, val: int) -> bool:
        if val not in self.ind:
            return False
        last_element = self.store[-1]
        last_ind = len(self.store) - 1
        val_ind = self.ind[val].pop(0)

        if val_ind != last_ind:
            self.store[val_ind] = last_element
            self.ind[last_element].remove(last_ind)
            self.ind[last_element].append(val_ind)
        self.store.pop()

        if not self.ind[val]:
            del self.ind[val]

        return True
        

    def getRandom(self) -> int:
        return random.choice(self.store)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()