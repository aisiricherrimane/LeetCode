class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        maxl = 0
        l = 0 
        for r in range(len(s)):
            letter = s[r]

            while s[r] in unique:
                unique.remove(s[l])
                l += 1
            unique.add(s[r])
            maxl = max(maxl, r - l + 1)
        return maxl
            





    