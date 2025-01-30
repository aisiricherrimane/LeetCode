class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

            
        longest = 1
        nums = set(nums)

        for i, n in enumerate(nums):
            if n - 1 in nums:
                continue
            l = 1
            while n + l in nums:
                l += 1
            longest = max(longest, l)
        return longest
        