class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(n + 1)}

        for s, d, w in times:
            adj[s].append((d, w))
        
        heap = [(0, k)]
        visit = set()
        t = 0

        while heap:
            weight, des = heapq.heappop(heap)

            if des in visit:
                continue
            visit.add(des)
            t = weight

            for neiD, neiW in adj[des]:
                heapq.heappush(heap, [neiW + weight, neiD])
        return t if len(visit) == n else -1
        

        