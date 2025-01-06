class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0
        prefix_sum = {0:1}
        count = 0
        for num in nums:
            current_sum += num
            if current_sum - k in prefix_sum:
                count += prefix_sum[current_sum - k]
            prefix_sum[current_sum] = 1 + prefix_sum.get(current_sum, 0)
        return count