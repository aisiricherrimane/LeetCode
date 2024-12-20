class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       nums.sort()

       l = 0 
       r = len(nums) - 1
       mid = r + l // 2
       return nums[mid]
