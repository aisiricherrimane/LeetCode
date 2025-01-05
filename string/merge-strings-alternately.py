class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        ans = ''

        while p1 < len(word1) and p2 < len(word2):
            ans = ans + word1[p1] + word2[p2]
            p1 += 1
            p2 += 1

        if p1 < len(word1):
            ans = ans + word1[p1:]
        else:
            ans = ans + word2[p2:]
        return ans
        