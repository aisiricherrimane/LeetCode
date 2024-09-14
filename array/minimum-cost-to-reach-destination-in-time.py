class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        adjM = collections.defaultdict(list)
        
        for x, y, t in edges:
            adjM[x].append([y, t])
            adjM[y].append([x, t])
        
        minH = [[passingFees[0], 0, 0]]
        visit = set()
        res = float('inf')

        while minH:
            cost, time, node = heapq.heappop(minH)
            if node in visit:
                continue
            if node == len(passingFees) - 1:
                res = min(res, cost)
            visit.add(node)
            
            for nei_city, nei_time in adjM[node]:
                if nei_city is not visit and time + nei_time <= maxTime:
                    heapq.heappush(minH, [cost + passingFees[nei_city], time + nei_time, nei_city])
        
        return res if res != float('inf') else -1







        