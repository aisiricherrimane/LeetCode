class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        subsum = 0
        res = 0
        for r in range(len(nums)):
            subsum += nums[r]
            while subsum > k:
                subsum -= nums[l]
                l += 1
            if subsum == k:
                res += 1
                
            
            
        return res
        