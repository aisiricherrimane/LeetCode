class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr = 0
        sign = 1

        for char in s:
            if char.isdigit():
                curr = curr * 10 + int(char)
            elif char == '+':
                stack.append(sign * curr)
                sign = 1
                curr = 0
            elif char == '-':
                stack.append(sign * curr)
                sign = -1
                curr = 0
            elif char == '(':
                stack.append(sign)
                stack.append('(')
                sign = 1
                curr = 0
            elif char == ')':
                stack.append(sign * curr)
                curr = 0

                res = 0
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.pop()
                sign = stack.pop()

                stack.append(sign * res)
                
        if curr != 0:
            stack.append(curr * sign)
        return sum(stack)
