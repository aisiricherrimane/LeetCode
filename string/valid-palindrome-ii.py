class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(l, r, changed):
            while l < r:
                if s[l] != s[r]:
                    if not changed:
                        return isPalindrome(l + 1, r, True) or isPalindrome(l, r - 1, True)
                    else:
                        return False
                else:
                    l += 1
                    r -= 1
            return True
        return isPalindrome(0, len(s) - 1, False)


        