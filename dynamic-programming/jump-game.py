class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i, jumps in enumerate(nums):
            if max_reach < i:
                return False
            max_reach = i + jumps
        return True