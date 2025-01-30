class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minL = min(len(word1), len(word2))
        i = 0
        res= ''
        while i < minL:
            res = res + word1[i] + word2[i]
            i += 1

        if i < len(word1):
            res += word1[i:] 
        else:
            res += word2[i:]

        return res
