class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        mean = sum(nums) / len(nums)
        ans = 0
        res = nums[0]
        for n in nums:
            if abs(mean - n) > ans:
                ans = abs(mean - n) 
                res = n
        return res
        