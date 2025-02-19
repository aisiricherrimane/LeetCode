class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0

        for r, num in enumerate(nums):
            k -= 1 - num

            while k < 0:
                k += 1 - nums[l]
                l += 1
            if k == 0:
                res = max(res, r - l + 1)
        return res
                

