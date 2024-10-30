class Solution:
    def compressedString(self, word: str) -> str:
        comp = ''
        i = 0

        while i < len(word):
            count = 0
            letter = word[i]
            while i < len(word) and word[i] == letter:
                count += 1
                i += 1
                if count == 9:
                    break
                    
            comp += str(count)
            comp += letter
        return comp


        