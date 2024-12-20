class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l = r = 0
        count = 0
        freq = {}

        while r < len(nums):
            freq[nums[r]] = 1 + freq.get(nums[r], 0)

            while max(freq) - min(freq) > 2:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1
            count += r - l + 1
            r += 1
        return count