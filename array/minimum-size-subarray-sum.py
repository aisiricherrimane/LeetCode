class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        sumi = 0
        length = float("inf")
        while r < len(nums):
            sumi += nums[r]
            while sumi >= target:
                length = min(length, r - l + 1)
                sumi -= nums[l]
                l += 1
            r += 1
        return 0 if length == float('inf') else length


            


        