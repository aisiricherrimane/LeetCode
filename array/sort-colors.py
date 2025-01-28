class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums) - 1):
            swapped = False
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    swapped = True
            if swapped == False:
                break
        return nums


        