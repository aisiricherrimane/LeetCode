class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        res = [n] * n 
        ind = []
        for i, char in enumerate(s):
            if char == c:
                ind.append(i)
        for i in range(len(s)):
            for a in ind:
                val = abs(i - a)
                res[i] = min(res[i], val)
        return res

        