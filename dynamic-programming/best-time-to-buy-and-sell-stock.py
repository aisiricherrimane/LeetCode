class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        profit = 0

        for price in prices:
            if price < lowest:
                lowest = price
            profit = max(profit, price - lowest)
        return profit
            