class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.res = 0  
        rows = m
        cols = n

        def dfs(r, c):
            if r >= 0 and r < rows and c >= 0 and c < cols:
                if r == m - 1 and c == n - 1:
                    self.res += 1
                    return 
                dfs(r + 1, c)
                dfs(r, c + 1)
        
        dfs(0, 0)
        return self.res

        