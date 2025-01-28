class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''

        minL = len(strs[0])

        for i in range(minL):
            for word in strs:
                if i >= len(word) or word[i] != strs[i]:
                    return res
            res += strs[i]
        return res


