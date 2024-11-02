class Solution:
   
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):  # Start from 1 since dp[0] is already set
            for c in coins:
                if a >= c and dp[a] > 1 + dp[a - c]:
                    dp[a] = 1 + dp[a - c]

        return dp[amount] if dp[amount] != (amount + 1) else -1
