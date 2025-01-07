class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        time = 0
        for i in range(0, len(nums), 3):
            if len(nums[i:]) == len(set(nums[i:])):
                return time
            time += 1
        return time
