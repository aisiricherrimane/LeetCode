class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        temp = 0

        for r in range(len(nums)):
            temp += nums[r]

            while temp > k:
                temp -= nums[l]
                l += 1
            
            if temp == k:
                res += 1
        return res
        