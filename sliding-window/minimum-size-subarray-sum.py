class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float('inf')
        sumi = 0
        r = 0
        l = 0
        while r < len(nums):
            sumi += nums[r]
            while sumi >= target:
                length = min(length, r - l + 1)
                sumi -= nums[l]
                l += 1
            r += 1
        return length if length != float('inf') else 0
        


