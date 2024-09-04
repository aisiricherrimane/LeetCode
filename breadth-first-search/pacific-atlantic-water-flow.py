class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        
        row = len(grid)
        col = len(grid[0])

        def dfs(r, c, visit, prevH):
            if r < 0 or c < 0 or r == row or c == col or (r,c) in visit or grid[r][c] < prevH:
                return 
            visit.add((r,c))
            dfs(r + 1, c, visit, grid[r][c])
            dfs(r - 1, c, visit, grid[r][c])
            dfs(r, c + 1, visit, grid[r][c])
            dfs(r, c - 1, visit, grid[r][c])

        for r in range(row):
            dfs(r, 0, pac, grid[r][0])
            dfs(r, col - 1, atl, grid[r][col - 1])

        for c in range(col):
            dfs(0, c, pac, grid[0][c])
            dfs(row - 1, c, atl, grid[row - 1][c]) 

        res = []
        for r in range(row):
            for c in range(col):
                if (r,c) in pac and (r, c) in atl:
                    res.append((r, c))
        return res
        
            
        