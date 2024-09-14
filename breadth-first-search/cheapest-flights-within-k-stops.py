class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjM = collections.defaultdict(list)

        for st, dt, c in flights:
            adjM[st].append([dt, c])
        
        s = 0
        visit = set()
        minH = [[0, 0, src]]

        while minH:
            cost, stop, place = heapq.heappop(minH)

            if place == dst:
                return cost
            if stop > k:
                continue
            visit.add(place)

            for neiS, neiC in adjM[place]:
                if neiS not in visit:
                    heapq.heappush(minH,[cost + neiC, stop + 1, neiS])
        return -1

            

        

