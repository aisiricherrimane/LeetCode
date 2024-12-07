class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        plength = len(p)
        pcount = Counter(p)
        window = Counter(s[:plength - 1])
        res = []

        for i in range(plength - 1, len(s)):
            window[s[i]] += 1
            if pcount == window:
                res.append(i - plength + 1)
            window[s[i - plength + 1]] -= 1
            if not window[s[i - plength + 1]]:
                del window[s[i - plength + 1]]
        return res




        