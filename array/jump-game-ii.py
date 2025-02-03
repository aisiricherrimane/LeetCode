class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_end = 0
        curr_far = 0
        count = 0

        for i in range(len(nums) - 1):
            curr_far = max(curr_far, i + nums[i])

            if i == curr_end:
                count += 1
                curr_end = curr_far
        return count