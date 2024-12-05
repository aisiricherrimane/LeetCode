class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return False
        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            else:
                if s[l + 1] == s[r]:
                    l = l + 2
                    r -= 1
                elif s[l] == s[r - 1]:
                    l = l + 1
                    r -= 2
                else:
                    return False
        return True
        