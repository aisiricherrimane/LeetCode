class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        adj = defaultdict(list)
        heap = []
        for i in range(len(points)):
            x1, y1 = points[i]
            dist = ((x1 ** 2) + (y1 ** 2)) ** 0.5
            heapq.heappush(heap, [dist, x1, y1])
        res = []
        while heap:
            d, x1, y1 = heapq.heappop(heap)
            if k > 0:
                res.append([x1, y1])
                k -= 1
            if k == 0:
                return res


                
        