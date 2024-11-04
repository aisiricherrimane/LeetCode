import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)  # Dimension of the grid
        minH = [(grid[0][0], 0, 0)]  # Start with the initial position in the heap
        visit = set()  # Set to keep track of visited positions
        
        while minH:
            height, r, c = heapq.heappop(minH)
            
            # Check if we have reached the bottom-right corner
            if r == n - 1 and c == n - 1:
                return height
            
            visit.add((r, c))  # Mark current position as visited
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Possible directions to move
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc  # Calculate new row and column
                
                # Check if the new position is within bounds and not yet visited
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visit:
                    # Push the maximum of the current height and the new cell height
                    heapq.heappush(minH, (max(height, grid[nr][nc]), nr, nc))
        
        return -1  # This line is just a safeguard; it should never be reached for valid input
