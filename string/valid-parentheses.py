class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = { ']' : '[', ")" : '(', '}' : '{'}

        for parenthesis in s:
            if parenthesis in check:
                if stack and stack[-1] == check[parenthesis]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(parenthesis)
        return True if not stack else False