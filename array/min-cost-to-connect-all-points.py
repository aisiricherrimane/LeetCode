class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append([j, dist])
                adj[j].append([i, dist])

        minH = [[0, 0]] # dist, 0
        visit = set()
        
        while len(visit) < n:
            
            dist, p = heapq.heappop(minH)

            if p == n:
                return dist
            fd = dist
            visit.add(p)

            for neiP, d in adj[p]:
                if neiP not in visit:
                    heapq.heappush(minH, [d + dist, neiP])

        return fd

                

            