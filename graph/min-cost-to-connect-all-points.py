class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((j, dist))
                adj[j].append((i, dist))
        minH = [[0, 0]]
        visit = set()
        res = 0

        while len(visit) < n:
            dist, p = heapq.heappop(minH)

            if p in visit:
                continue
            
            visit.add(p)
            res += dist
 
            for neiP, neid in adj[p]:
                if neiP not in visit:
                    heapq.heappush(minH, [neid, neiP])

        return res
        
               