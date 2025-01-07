class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        largest = None
        total = sum(nums)
        lookup = set(nums)

        for num in nums:
            sp = total - num  # Calculate the potential sum of special numbers

            # Check if sp is valid and distinct from the current num
            if sp in lookup and sp != num:
                if largest is None:
                    largest = num
                else:
                    largest = max(largest, num)  # Update largest with the outlier (num), not sp

        # Since the problem guarantees at least one outlier, largest cannot remain None
        return largest
