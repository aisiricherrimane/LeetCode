class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
            
        x = 1
        for i in nums:
            x = x * i

        if x > 0:
            return 1
        elif x < 0:
            return -1

        