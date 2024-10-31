class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alphanum(w):
            if ord('a') <= ord(w) <= ord('z') or ord('A') <= ord(w) <= ord('Z') or ord('1') <= ord(w) <= ord('9'):
                return True
            else:
                return False
            
        
        l = 0 
        r = len(s) - 1

        while l < r:
            while l < r and not alphanum(s[l]):
                l += 1
            while l < r and not alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
