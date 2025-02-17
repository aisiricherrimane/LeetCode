class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        temp = {0:1}
        curr_num = 0
        subs = 0

        for i in range(len(nums)):
            curr_num += nums[i]
            if curr_num - k in temp:
                subs += temp[curr_num - k]
            
            temp[curr_num] = 1 + temp.get(curr_num, 0)
        return subs
        