class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sub = []

        def bactrack(opened, closed):
            if opened == closed == n:
                res.append(''.join(sub))
                return 
            if opened < n:
                sub.append('(')
                bactrack(opened + 1, closed)
                sub.pop()
            if closed < opened:
                sub.append(')')
                bactrack(opened, closed + 1)
                sub.pop()
        
        bactrack(0, 0)
        return res


        