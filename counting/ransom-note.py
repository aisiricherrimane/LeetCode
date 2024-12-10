class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magC = Counter(magazine)
        ransomNote_c = Counter(ransomNote)

        for char in ransomNote_c:
            if ransomNote_c[char] > magC[char]:
                return False
        return True