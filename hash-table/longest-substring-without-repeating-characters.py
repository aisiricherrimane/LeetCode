class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        length = 0
        temp = set()
        for r in range(len(s)):
            letter = s[r]

            while s[r] in temp:
                temp.remove(s[l])
                l += 1
            temp.add(s[r])
            length = max(length, r - l + 1)
        return length



    