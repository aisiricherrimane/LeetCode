class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        l = 0
        for r in range(len(nums)):
            while nums[r] != nums[l]:
                l += 1
            if r - l + 1 > len(nums) // 2:
                return nums[r]
        return -1


        