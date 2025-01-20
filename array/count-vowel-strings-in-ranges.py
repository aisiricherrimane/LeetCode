from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Step 1: Calculate vowel counts for each word
        vowel_count = [0] * len(words)

        for ind, s in enumerate(words):
            vowel_count[ind] = sum(1 for char in s if char in 'aeiou')

        # Step 2: Process each query
        res = [sum(vowel_count[s:e + 1]) for s, e in queries]
        return res
