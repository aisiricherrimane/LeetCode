class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count_char = Counter(chars)
        res = 0
        for word in words:
            curr_count = Counter(word)
            for letter in curr_count:
                if curr_count[letter] > count_char.get(letter, 0):
                    break
            else:
                res += len(word)
        return res



        