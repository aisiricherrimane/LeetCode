class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxl = height[l]
        maxr = height[r]
        val = 0
        while l < r:
            if maxl < maxr:
                l += 1
                maxl = max(maxl, height[l])
                val += maxl - height[l]
            else:
                r -= 1
                maxr = max(maxr, height[r])
                val += maxr - height[r]

        return val
