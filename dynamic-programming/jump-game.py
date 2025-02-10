class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0

        for i, n in enumerate(nums):
            if max_jump < i:
                return False
            max_jump = max(max_jump, i + n)
            if max_jump >= len(nums):
                break
        return True