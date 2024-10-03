import heapq
import collections

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = collections.defaultdict(list)
        
        # Build the adjacency list
        for s, d, p in flights:
            adj[s].append((d, p))
        
        # Min heap: (cost, current place, stops)
        minH = [(0, src, 0)]
        
        # Dictionary to track the minimum cost to reach each node with up to a certain number of stops
        costs = {(src, 0): 0}
        
        while minH:
            cost, place, stops = heapq.heappop(minH)
            
            # If destination is reached, return the cost
            if place == dst:
                return cost
            
            # If stops exceed k, continue to the next iteration
            if stops > k:
                continue
            
            # Explore the neighbors
            for nei, nei_cost in adj[place]:
                new_cost = cost + nei_cost
                
                # Only add to heap if it's a cheaper path or we've used fewer stops
                if (nei, stops + 1) not in costs or new_cost < costs[(nei, stops + 1)]:
                    costs[(nei, stops + 1)] = new_cost
                    heapq.heappush(minH, (new_cost, nei, stops + 1))
        
        # If destination cannot be reached, return -1
        return -1
