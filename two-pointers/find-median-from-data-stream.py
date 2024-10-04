class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        
    def addNum(self, num: int) -> None:
          
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)
        
        if len(self.small) + 1 > len(self.large):
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)
        elif len(self.large) + 1 > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            mean = ((-1 * self.small[0]) + self.large[0]) / 2
            return mean

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()