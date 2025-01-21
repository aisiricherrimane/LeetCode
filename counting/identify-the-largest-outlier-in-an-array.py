class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        sum_v = sum(nums)
        num_count = Counter(nums)
        largest_outlier = float('-inf')

        for num in num_count.keys():
            possible = sum_v - 2 * num

            if possible in num_count:
                if possible != num or num_count[num] > 1:
                    largest_outlier = max(largest_outlier, possible)
        return largest_outlier



        