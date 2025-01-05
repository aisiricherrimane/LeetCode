class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, number in enumerate(nums):
            if i > 0 and nums[i - 1] == number:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threesum = nums[l] + nums[r] + number
                if threesum > 0:
                    r -= 1
                elif threesum < 0 :
                    l += 1
                else:
                    res.append([nums[l], nums[r], number])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res