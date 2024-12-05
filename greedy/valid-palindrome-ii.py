class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return False
        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                s1 = s[l + 1 : r + 1]
                s2 = s[l : r]
                return s1 == s1[::-1] or s2 == s2[::-1]
            l += 1
            r -= 1
        return True
                
        