class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        sub = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append(''.join(sub))
                return
            if openN < n:
                sub.append('(')
                backtrack(openN + 1, closeN)
                sub.pop()
            if closeN < openN:
                sub.append(')')
                backtrack(openN, closeN + 1)
                sub.pop()
        backtrack(0, 0)
        return res
