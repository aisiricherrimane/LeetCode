class Solution:
    def firstUniqChar(self, s: str) -> int:
        temp = {}
        for i in s:
            temp[i] = 1 + temp.get(i, 0)
        for i in range(len(s)):
            if temp[s[i]] == 1:
                return i
                break
        return -1

        