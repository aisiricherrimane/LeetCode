from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0] * (len(words) + 1)

        for i, word in enumerate(words):
            if word[0] in 'aeiou' and word[-1] in 'aeiou':
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i] 
        
        res = []

        for l, r in queries:
            res.append(prefix[r + 1] - prefix[l])

        return res

        

