class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char = Counter(chars)
        res = 0
        for word in words:
            count_word = Counter(word)
            for w in count_word:
                if count_word[w] > char.get(w, 0):
                    break
            else:
                res += len(word)
        return res

        