class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in temp:
                return [i, temp[diff]]
            temp[n] = i
        return -1