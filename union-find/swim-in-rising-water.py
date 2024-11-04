class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minH = [[grid[0][0], 0, 0]]
        visit = set()

        while minH:
            height, r, c = heapq.heappop(minH)

            if r == n - 1 and c == n - 1:
                return height
            visit.add((r, c))

            directions = [[0,1],[1,0],[0, -1], [-1, 0]]
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visit:
                    heapq.heappush(minH, [max(height, grid[nr][nc]), nr, nc])
        return -1
        


