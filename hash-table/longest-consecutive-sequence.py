class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        i = 0
        for i in nums:
            if i - 1 not in nums:
                l = 1
                while i + l in nums:
                    l += 1
                longest = max(longest, l)
        return longest



        