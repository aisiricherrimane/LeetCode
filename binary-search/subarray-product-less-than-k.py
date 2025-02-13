class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: 
            return 0

        res = 0 
        l = 0
        running_prod = 1
        for r, n in enumerate(nums):
            running_prod *= n

            while running_prod >= k and l <= r:
                running_prod = running_prod / nums[l]
                l += 1
            res += (r - l + 1)
        return res





        