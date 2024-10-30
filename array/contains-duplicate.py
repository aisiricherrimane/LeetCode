class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = set()
        for n in nums:
            if n not in temp:
                temp.add(n)
            else:
                return True
        return False
        