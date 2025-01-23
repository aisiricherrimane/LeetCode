class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1

        for i, n in enumerate(nums):
            if n - 1 not in nums:
                l = 1
                while n + l in nums:
                    l += 1
                longest = max(l, longest)
        return longest
        