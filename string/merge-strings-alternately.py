class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = 0
        l2 = 0
        res = ''
        while l1 < len(word1) and l2 < len(word2):
            res = res + word1[l1] + word2[l2]
            l1 += 1
            l2 += 1
        
        if l1 < len(word1):
            res = res + word1[l1:]
        else:
            res = res + word2[l2:]
        
        return res
            