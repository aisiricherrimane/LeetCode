class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            ans = max(ans, curr_sum)
        return ans



        
        