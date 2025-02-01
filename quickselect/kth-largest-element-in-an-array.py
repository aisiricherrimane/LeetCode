from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k  # Convert k-th largest to index

        def quickSelect(l, r):
            pivot, p = nums[r], l  # Pick last element as pivot
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]  # Swap elements
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]  # Place pivot in correct position

            if p > k: 
                return quickSelect(l, p - 1)  # Search left part
            elif p < k:
                return quickSelect(p + 1, r)  # Search right part
            else:
                return nums[p]  # Found the k-th largest element

        return quickSelect(0, len(nums) - 1)
