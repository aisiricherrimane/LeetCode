import heapq
import collections

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjM = collections.defaultdict(list)

        # Build the adjacency list from flights
        for st, dt, c in flights:
            adjM[st].append([dt, c])

        # Min-heap where each entry is [cost, stops, node]
        minH = [[0, 0, src]]
        
        # Dictionary to track the minimum stops required to reach each node
        best = {}

        while minH:
            cost, stop, place = heapq.heappop(minH)

            # If we reached the destination, return the cost
            if place == dst:
                return cost
            
            # If we have exceeded the allowed number of stops, skip this path
            if stop > k:
                continue
            
            # If we've visited this node before with fewer or equal stops, skip it
            if place in best and best[place] <= stop:
                continue
            
            # Update the best known stops to reach this node
            best[place] = stop
            
            # Add neighbors to the heap
            for nei, price in adjM[place]:
                heapq.heappush(minH, [cost + price, stop + 1, nei])

        # If no valid path is found, return -1
        return -1
