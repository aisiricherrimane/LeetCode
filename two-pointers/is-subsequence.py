class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        countS = 0
        countT = 0
        while countS < len(s) and countT < len(t):
            if s[countS] == t[countT]:
                countS += 1
            countT += 1
        return countS == len(s)  