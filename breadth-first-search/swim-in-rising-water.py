import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        visit = set()
        minH = [[grid[0][0], 0, 0]]
        n = len(grid)
        visit.add((0, 0))

        while minH:
            height, r, c = heapq.heappop(minH)

            if r == n - 1 and c == n - 1:
                return height
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = dr + r, dc + c
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visit:
                    heapq.heappush(minH, (max(height, grid[nr][nc]), nr, nc))
                    visit.add((nr, nc))




        return -1