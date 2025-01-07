class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        temp = set(nums)
        temp.remove(0)
        return len(temp)


        