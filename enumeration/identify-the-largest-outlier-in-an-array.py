class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        nums_counts = Counter(nums)

        largest_outlier = float('-inf')

        for num in nums_counts.keys():
            potential = total_sum - 2 * num

            if potential in nums_counts:
                if potential != num or nums_counts[num] > 1:
                    largest_outlier = max(largest_outlier, potential)
        return largest_outlier


        