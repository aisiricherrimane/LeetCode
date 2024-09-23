class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        curr_sum = 0
        res = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if nums[i] > curr_sum:
                curr_sum = nums[i]
            res = max(res, curr_sum)
        return res



        
        