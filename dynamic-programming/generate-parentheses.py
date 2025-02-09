class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sub = []
        def backtrack(openP, closeP):
            if openP == closeP == n:
                res.append(''.join(sub))
                return 
            if openP < n:
                sub.append('(')
                backtrack(openP + 1, closeP)
                sub.pop()
            if openP > closeP:
                sub.append(')')
                backtrack(openP, closeP + 1)
                sub.pop()
            
        backtrack(0, 0)
        return res

