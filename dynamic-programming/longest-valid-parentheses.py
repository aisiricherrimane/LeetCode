class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def check(string):
            stack = []
            for p in string:
                if p == '(':
                    stack.append('(')
                elif stack and stack[-1] == '(':
                    stack.pop()
                else:
                        return False

            return len(stack) == 0

        maxl = 0
        for i in range(len(s)):
            for j in range(i + 2, len(s) + 1, 2):
                if check(s[i:j]):
                    maxl = max(maxl, j - i)

        return maxl

    
                

        