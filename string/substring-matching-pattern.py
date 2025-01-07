class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        mid = p.index('*')

        left = s.find(p[:mid])
        if left == -1:
            return False
        
        right = s[left + len(p[:mid]) - 1:].find(p[mid + 1:])
        if right == -1:
            return False
        return True

