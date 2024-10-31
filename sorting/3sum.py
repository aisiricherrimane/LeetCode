class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                thr_sum = nums[l] + nums[r] + n

                if thr_sum < 0:
                    l += 1
                elif thr_sum > 0:
                    r -= 1
                else:
                    res.append([nums[l], nums[r], n])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res




