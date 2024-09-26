class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        directions = [(0, 1),(0, -1),(-1, 0),(1, 0)]

        def dfs(r, c):
            grid[r][c] = "0"
            for dr, dc in directions:
                R = r + dr
                C = c + dc
                if R >= 0 and R < rows and C >= 0 and C < cols and grid[R][C] =='1':
                    dfs(R, C)
            return
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1
        return islands

    
        