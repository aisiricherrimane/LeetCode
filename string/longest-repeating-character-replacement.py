class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        maxf = 0
        temp = {}
        for r in range(len(s)):
            temp[s[r]] = 1 + temp.get(s[r], 0)
            maxf = max(maxf, temp[s[r]])

            while (r - l + 1) - maxf > k:
                temp[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

            


        