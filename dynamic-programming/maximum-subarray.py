class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = curr_sum = nums[0]

        for r in nums[1:]:
            curr_sum = max(curr_sum + r, r)
            max_sum = max(max_sum, curr_sum)
        return max_sum