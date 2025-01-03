class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        mean = sum(nums) / len(nums)
        max_diff = 0
        outlier = nums[0]
        
        for n in nums:
            diff = abs(mean - n)
            if diff > max_diff:
                max_diff = diff
                outlier = n
        
        return outlier