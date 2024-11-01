class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        islands = 0
        directions = [(1, 0), (-1, 0), (0 , 1), (0, -1)]
        

        def dfs(r, c):
            grid[r][c] = "0"
            for dr, dc in directions:
                newR = dr + r
                newC = dc + c
                if newR >= 0 and newR < row and newC >= 0 and newC < col and grid[newR][newC] == '1':
                    dfs(newR, newC)
            


        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1
        return islands


        

        