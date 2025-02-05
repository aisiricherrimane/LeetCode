class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part[:])
                return 
            for j in range(i, len(s)):
                if self.pali(s[i:j + 1]):
                    part.append(s[i:j + 1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res
    
    def pali(self, c):
        return c == c[::-1]
               