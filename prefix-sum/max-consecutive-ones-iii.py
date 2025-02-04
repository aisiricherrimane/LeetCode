class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0

        for r in range(len(nums)):
            k -= 1 - nums[r]

            if k < 0:
                k += 1 - nums[left]
                left += 1
        return r - left + 1

            


        