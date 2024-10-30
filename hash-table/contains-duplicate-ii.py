class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        temp = {}
        for i,n in enumerate(nums):
            if n in temp:
                present_ind = temp[n]
                if abs(i - present_ind) <= k:
                    return True
                else:
                    temp[n] = i
            else:
                temp[n] = i
        return False