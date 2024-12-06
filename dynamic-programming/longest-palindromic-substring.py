class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        res_pair = [-1, -1]
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                if res < r - l + 1:
                    res = r - l + 1
                    res_pair = [l, r]
                l -= 1
                r += 1
            
            l = i
            r = i + 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                if res < r - l + 1:
                    res = r - l + 1
                    res_pair = [l, r]
                l -= 1
                r += 1
        l, r= res_pair
        return s[l : r + 1]


        