class Solution:
    def jump(self, nums: List[int]) -> int:
        answer = 0
        n = len(nums)

        curr_end = 0
        curr_far = 0

        for i in range(n - 1):
            curr_far = max(curr_far, nums[i] + i)

            if i == curr_end:
                answer += 1
                curr_end = curr_far
        return answer
        