class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjM = {i:[] for i in range(1, n+1)}

        for s, d, t in times:
            adjM[s].append([d, t])
        
        visit = set()
        minH = [[0, k]]
        visit.add(k)

        while minH:
            t, p = heapq.heappop(minH)
            if len(visit) == n:
                return t
            for neiD, neiT in adjM[p]:
                if neiD not in visit:
                    heapq.heappush(minH, [t + neiT, neiD])
                    visit.add(neiD)
        return -1




        