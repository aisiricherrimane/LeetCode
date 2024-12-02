class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = set()
        for n in nums:
            if n in temp:
                return True
            else:
                temp.add(n)
        return False
        