class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()

        l = 0
        r = len(s) - 1

        while l < len(s) and r >= 0 and l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ' '.join(s)