class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        if obstacleGrid[row - 1][col - 1] == 1:
            return 0
            
        dp = [[1] * col for _ in range(row)]
        
        for r in range(1, row):
            for c in range(1, col):
                if obstacleGrid[r][c] == 1:
                    continue
                if obstacleGrid[r - 1][c] == 1:
                    dp[r - 1][c] = 0
                if obstacleGrid[r][c - 1] == 1:
                    dp[r][c - 1] = 0
                
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[row - 1][col - 1]