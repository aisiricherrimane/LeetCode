class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien = {char:i for i, char in enumerate(order)}
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if alien[word1[j]] > alien[word2[j]]:
                        return False
                    else:
                        break
            
            else:
                if len(word1) > len(word2):
                    return False
        return True                

        