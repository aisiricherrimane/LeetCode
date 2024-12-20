class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums
        l = 0
        r = l + 1

        while r < len(nums):
            while nums[l] != 0:
                l += 1
            while r < len(nums) and nums[r] == 0:
                r += 1
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l += 1
            r += 1
        return nums
        