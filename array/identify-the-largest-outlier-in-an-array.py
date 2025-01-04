class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums)
        unique = set(nums)
        res = float('-inf')

        for num in nums:
            pottential_sum = total - num
            
            if pottential_sum - num in unique:
                res = max(res, num)
        return res