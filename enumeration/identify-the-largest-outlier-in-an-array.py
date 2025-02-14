class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        largest_outlier = float('-inf')
        num_count = Counter(nums)
        total = sum(nums)

        for i, n in enumerate(nums):
            possible_outlier = total - (2 * n)

            if possible_outlier in num_count:
                if possible_outlier != n or num_count[n] > 1:
                    largest_outlier = max(largest_outlier, possible_outlier)
        return largest_outlier

