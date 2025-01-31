class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        row = len(grid)
        col = len(grid[0])

        def dfs(r, c):
            if r >= 0 and r < row and c >= 0 and c < col and grid[r][c] == '1':
                grid[r][c] = '0'
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1
        return islands
        