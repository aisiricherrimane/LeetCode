class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        temp = [0] * (len(words) + 1)

        for i, w in enumerate(words):
            if w[0] in 'aeiou' and w[-1] in'aeiou':
                temp[i + 1] = temp[i] + 1
            else:
                temp[i + 1] = temp[i]

        res = []
        for l, r in queries:
            res.append(temp[r + 1] - temp[l])
        return res
