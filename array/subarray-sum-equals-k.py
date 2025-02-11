class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subs = 0
        sum_freq = {0:1}
        curr_sum = 0

        for num in nums:
            curr_sum += num

            if curr_sum - k in sum_freq:
                subs += sum_freq[curr_sum - k]
            
            sum_freq[curr_sum] = 1 + sum_freq.get(curr_sum, 0)
        return subs