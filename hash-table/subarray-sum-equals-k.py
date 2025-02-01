class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subs = 0
        cumm_freq = {0 : 1}
        curr_sum = 0

        for num in nums:
            curr_sum += num
            if curr_sum - k in cumm_freq:
                subs += cumm_freq[curr_sum - k]
            cumm_freq[curr_sum] = 1 + cumm_freq.get(curr_sum, 0)
        return subs

