class HitCounter:

    def __init__(self):
        self.store = deque()
        self.l = 0
    def hit(self, timestamp: int) -> None:
        self.store.append(timestamp)
        self.l += 1
    def getHits(self, timestamp: int) -> int:
        while self.store and timestamp - self.store[0] >= 300:
            self.store.popleft()
            self.l -= 1
        return self.l 
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)