class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        res = 0
        for word in words:
            curr_count = Counter(word)
            for w in curr_count:
                if curr_count[w] > char_count[w]:
                    break
            else:
                res += len(word)
        return res

       



        