class Solution:
    def compressedString(self, word: str) -> str:
        i = 0
        res = ''
        while i < len(word):
            letter = word[i]
            count = 0
            while i < len(word) and word[i] == letter:
                count += 1
                i += 1
                if count > 8:
                    break
            res = res + str(count) + letter
        return res