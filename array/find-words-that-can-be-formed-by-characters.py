class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        res = 0
        for word in words:
            count = Counter(word)
            for c in count:
                if count[c] > chars_count[c]:
                    break
            else:
                res += len(word)
        return res


       



        