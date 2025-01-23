class HitCounter:

    def __init__(self):
        self.queue = collections.deque()
        self.sum = 0
        

    def hit(self, timestamp: int) -> None:
        while self.queue and timestamp - self.queue[0] >= 300:
            self.queue.popleft()
            self.sum -= 1
        self.queue.append(timestamp)
        self.sum += 1
        

    def getHits(self, timestamp: int) -> int:
        while self.queue and timestamp - self.queue[0] >= 300:
            self.queue.popleft()
            self.sum -= 1
        return self.sum
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
