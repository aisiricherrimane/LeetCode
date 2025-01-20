from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0] * len(words)

        for i, word in enumerate(words):
            if word[0] in 'aeiou' and word[-1] in 'aeiou':
                prefix[i] = 1

        res = [0] * len(queries)
        i = 0
        for s, e in queries:
            res[i] = sum(prefix[s:e + 1])
            i += 1
        return res

        

