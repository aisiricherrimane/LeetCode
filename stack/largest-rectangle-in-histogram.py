class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxA = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                ind, height = stack.pop()
                maxA = max(maxA, (i - ind) * height)
                start = ind
            stack.append((start, h))
        
        while stack:
            ind, height = stack.pop()
            maxA = max(maxA, (len(heights) - ind) * height)
        return maxA

