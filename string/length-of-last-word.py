class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp = s.strip().split()
        if not temp:
            return 0
        return len(temp[-1])