class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        rows = len(heights)
        cols = len(heights[0])

        def dfs(r, c, visit, preV):
            if 0 <= r < rows and 0 <= c < cols and (r, c) not in visit and heights[r][c] >= preV:
                visit.add((r, c))
                dfs(r + 1, c, visit, heights[r][c])
                dfs(r - 1, c, visit, heights[r][c])
                dfs(r, c + 1, visit, heights[r][c])
                dfs(r, c - 1, visit, heights[r][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append((r, c))
        return res
