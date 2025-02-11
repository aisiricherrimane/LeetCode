class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        left, curr_sum, count = 0, 0, 0

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum > k and left <= right:
                curr_sum -= nums[left]
                left += 1

            if curr_sum == k:
                count += 1  # Found a valid subarray

        return count