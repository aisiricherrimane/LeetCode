class Solution:
    def isPalindrome(self, s: str) -> bool:
        def check(c):
            if ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9'):
                return True
            else:
                return False
        
        l = 0
        r = len(s) - 1
        while l <= r:
            while l < r and not check(s[l]):
                l += 1
            while l < r and not check(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
