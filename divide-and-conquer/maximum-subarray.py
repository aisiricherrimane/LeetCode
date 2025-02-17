class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = float('-inf')
        curr_val = 0

        for n in nums:
            curr_val = max(curr_val + n, n)

            max_val = max(max_val, curr_val)
        return max_val

        