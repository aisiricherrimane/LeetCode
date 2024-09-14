import heapq
import collections

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        adjM = collections.defaultdict(list)
        
        # Create adjacency list from edges
        for x, y, t in edges:
            adjM[x].append([y, t])
            adjM[y].append([x, t])
        
        # Min-heap (priority queue), where we store [cost, time, node]
        minH = [[passingFees[0], 0, 0]]  # start from node 0
        
        # Set to track visited states as (node, time)
        visit = set()
        
        res = float('inf')

        while minH:
            cost, time, node = heapq.heappop(minH)
            
            # If the time exceeds maxTime, skip this path
            if time > maxTime:
                continue
            
            # If we've reached the destination and within maxTime, update result
            if node == len(passingFees) - 1:
                res = min(res, cost)
            
            # Mark the node and time as visited
            visit.add((node, time))
            
            # Process neighbors
            for nei_city, nei_time in adjM[node]:
                new_time = time + nei_time
                new_cost = cost + passingFees[nei_city]

                # Allow revisiting only if the new state (node, time) is not visited
                if (nei_city, new_time) not in visit:
                    heapq.heappush(minH, [new_cost, new_time, nei_city])

        # If a valid result was found, return it, otherwise return -1
        return res if res != float('inf') else -1
