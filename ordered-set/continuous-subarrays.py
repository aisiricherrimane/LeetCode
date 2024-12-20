class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l = 0
        r = 0 
        count = 0
        store = []
        while r < len(nums):
            store.append(nums[r])

            while max(store) - min(store) > 2:
                store.remove(nums[l])
                l += 1
            count += r - l + 1
            r += 1
        return count




        