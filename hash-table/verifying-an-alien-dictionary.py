class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letter_map = {char:i for i, char in enumerate(order)}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            for k in range(min(len(word1), len(word2))):
                if word1[k] != word2[k]:
                    if letter_map[word1[k]] > letter_map[word2[k]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True