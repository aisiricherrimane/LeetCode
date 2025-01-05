class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [-1, -1]
        resl = 0

        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                if r - l + 1 > resl:
                    resl = r - l + 1
                    res = [l, r]
                l -= 1
                r += 1
            l = i
            r = i + 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                if r - l + 1 > resl:
                    resl = r - l + 1
                    res = [l, r]
                l -= 1
                r += 1
        l, r = res
        return s[l:r + 1]
        