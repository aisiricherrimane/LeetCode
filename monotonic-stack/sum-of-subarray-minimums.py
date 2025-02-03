class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        sum_min_subs = 0
        stack = []

        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                right = i
                # number of subarrays
                count = (mid - left) * (right - mid)
                sum_min_subs += (count * arr[mid])
            stack.append(i)
        return sum_min_subs
        