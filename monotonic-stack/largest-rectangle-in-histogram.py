class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i,h in enumerate(heights):
            start = i

            while stack and h < stack[-1][1]:
                ind, height = stack.pop()
                res = max(res, (i - ind) * height)
                start = ind
            stack.append((start, h))
        
        while stack:
            ind, height = stack.pop()
            res = max(res, (len(heights) - ind) * height)
        return res
                
