class HitCounter:

    def __init__(self):
        self.q = deque()
        self.count = 0

    def hit(self, timestamp: int) -> None:
        self.count += 1
        self.q.append([timestamp, count])
        
    def getHits(self, timestamp: int) -> int:
        while self.q and timestamp - self.q[0][0] >= 300:
            self.q.popleft()
            self.count -= 1
        return self.count 

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)