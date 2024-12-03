class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxr = height[r]
        maxl = height[l]
        res = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                maxl = max(maxl, height[l])
                res += maxl - height[l]
            else:
                r -= 1
                maxr = max(maxr, height[r])
                res += maxr - height[r]
        return res

