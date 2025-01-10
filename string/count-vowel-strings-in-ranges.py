class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix  = [0] * (len(words) + 1)
        vowels = ['a', 'e', 'i', 'o', 'u']

        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i]
        
        result = []
        for l, r in queries:
            result.append(prefix[r + 1] - prefix[l])
        return result

