class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin = 1
        currMax = 1

        for n in nums:
            if n == 0:
                currMin = 1
                currMax = 1
            temp = currMax * n
            currMax = max(currMin * n, currMax * n, n)
            currMin = min(temp, currMin * n, n)
            res = max(res, currMax, currMin)
        return res



        