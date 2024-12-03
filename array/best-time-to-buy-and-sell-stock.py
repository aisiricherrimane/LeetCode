class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        lp = prices[l]
        for price in prices:
            if price < lp:
                lp = min(lp, price)
            profit = max(profit, price - lp)
        return profit