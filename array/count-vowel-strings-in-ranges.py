class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        temp = [0] * len(words)

        for i, w in enumerate(words):
            if w[0] in 'aeiou' and w[-1] in'aeiou':
                temp[i] = 1
        res = []
        for l, r in queries:
            res.append(sum(temp[l:r + 1]))
        return res
