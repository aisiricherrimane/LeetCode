class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        low = nums[l]
        while l <= r:
            if nums[l] < nums[r]:
                return min(low, nums[l])
            mid = (l + (r - l)) // 2
            low = min(low, nums[mid])
            
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return low
