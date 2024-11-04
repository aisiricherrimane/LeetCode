class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)

        for s, d, w in times:
            adj[s].append((d, w))

        minH = [(0, k)]
        visit = set()
        t = 0
        while minH:
            weight, des = heapq.heappop(minH)
            if des in visit:
                continue
            visit.add(des)
            t = weight

            for neiN, neiW in adj[des]:
                if neiN not in visit:
                    heapq.heappush(minH, [weight+neiW, neiN])
        return t if len(visit) == n else -1



        