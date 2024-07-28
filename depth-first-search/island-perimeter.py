class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        self.cnt = 0
        def dfs(r, c):
            if r < 0 or r > row - 1 or c < 0 or c > col - 1:
                return 1
            elif grid[r][c] == 0:
                return 1
            elif grid[r][c] == -1:
                return 0
            else:
                grid[r][c] = -1
                return dfs(r + 1,c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return dfs(r, c)

                    

        