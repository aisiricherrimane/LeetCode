class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = Counter(magazine)

        ran = Counter(ransomNote)

        for r in ran:
            if ran[r] > mag[r]:
                return False
        return True
                
        