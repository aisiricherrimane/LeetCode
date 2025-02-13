class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        nums = set(nums)
        for i, n in enumerate(nums):
            if n - 1 in nums:
                continue
            l = 1
            while l + n in nums:
                l += 1
            length = max(l, length)
        return length