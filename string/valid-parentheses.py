class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check ={ ']' : '[', ")" : '(', '}' : '{'}

        for p in s:
            if p in check:
                if stack and stack[-1] == check[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return True if not stack else False

        