class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = len(nums)/2
        temp = {}
        for n in nums:
            if n in temp:
                temp[n] += 1
            else:
                temp[n] = 1
        
        for n, c in temp.items():
            if c > d:
                return n
        return -1
                    