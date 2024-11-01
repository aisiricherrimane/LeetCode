class RandomizedCollection:

    def __init__(self):
        self.store = []
        self.ind = collections.defaultdict(list)

    def insert(self, val: int) -> bool:
        self.ind[val].append(len(self.store))
        self.store.append(val)

        return len(self.ind[val]) == 1

    def remove(self, val: int) -> bool:
        if val not in self.ind or not self.ind[val]:
            return False

        last_element = self.store[-1]
        ind_to_switch = self.ind[val].pop(0)
        if ind_to_switch != len(self.store) - 1:
            self.store[ind_to_switch] = last_element

            self.ind[last_element].remove(len(self.store) - 1)
            self.ind[last_element].append(ind_to_switch )
        self.store.pop()

        if not self.ind[val]:
            del self.ind[val]

        return True

    def getRandom(self) -> int:
        return choice(self.store)
        
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()