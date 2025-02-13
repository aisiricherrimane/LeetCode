class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) < k:
            return None
        
        heap = []

        for x1, y1 in points:
            dist = (x1 ** 2 + y1 ** 2) ** 0.5
            heapq.heappush(heap, [dist, (x1, y1)])

        res = []
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res

        