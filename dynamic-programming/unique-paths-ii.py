class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[row - 1][col - 1] == 1:
            return 0

        dp = [[0] * col for _ in range(row)]
        dp[0][0] = 1 
        
        for r in range(row):
            for c in range(col):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0  # No path if there's an obstacle
                else:
                    if r > 0:
                        dp[r][c] += dp[r - 1][c]
                    if c > 0:
                        dp[r][c] += dp[r][c - 1]

        return dp[row - 1][col - 1]