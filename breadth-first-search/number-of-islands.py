class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            grid[r][c] = ''
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                R, C = dr + r, dc + c
                if 0 <= R < rows and 0 <= C < cols and grid[R][C] == '1':
                    dfs(R, C)
            return 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1
        return islands