class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[l]
        while l <= r:
            if nums[l] < nums[r]:
                return min(res, nums[l])
            mid = r + l // 2
            res = min(res, nums[mid])
            
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return res
