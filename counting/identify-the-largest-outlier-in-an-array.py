class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        num_count = Counter(nums)
        largest_outlier = float('-inf')

        for n in nums:
            possible_outlier = total_sum - (2 * n)

            if possible_outlier in num_count:
                if possible_outlier != n or num_count[n] > 1:
                    largest_outlier = max(largest_outlier, possible_outlier)
        return largest_outlier

            

        