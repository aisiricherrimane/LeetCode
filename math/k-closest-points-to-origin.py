class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []

        for x, y in points:
            dist = (x ** 2 + y ** 2) ** 0.5
            heapq.heappush(minheap, [dist, [x, y]])
        res = []
        while k != 0:
            dist, pt = heapq.heappop(minheap)
            res.append(pt)
            k -= 1
        return res



       