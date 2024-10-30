class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexM = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indexM:
                return indexM[diff], i
            else:
                indexM[n] = i
        return -1

        