class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0

        l = 0
        curr = 1
        for r,n in enumerate(nums):
            curr *= nums[r]

            while curr >= k and l <= r:
                curr = curr / nums[l]
                l += 1

            res += (r - l+ 1)
        return res
        

        





        