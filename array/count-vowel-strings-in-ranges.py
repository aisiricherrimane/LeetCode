class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel_count = [0] * (len(words) + 1 )

        for i, w in enumerate(words):
            if w[0] in 'aeiou' and w[-1] in 'aeiou':
                vowel_count[i + 1] = 1 + vowel_count[i]
            else:
                vowel_count[i + 1] = vowel_count[i]
        res = []
        for l, r in queries:
            res.append(vowel_count[r + 1] - vowel_count[l])
        return res

