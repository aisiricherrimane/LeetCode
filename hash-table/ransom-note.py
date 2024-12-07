class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_count = Counter(magazine)
        ran_count = Counter(ransomNote)

        for l in ran_count:
            if ran_count[l] > mag_count[l]:
                return False
        return True
                
        