class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if i > 0 and nums[i - 1] == n:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                threesum = n + nums[l] + nums[r]
                if threesum < 0:
                    l += 1
                elif threesum > 0:
                    r -= 1
                else:
                    res.append([nums[l], nums[r], n])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res




