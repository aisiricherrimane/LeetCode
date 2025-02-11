class Solution:
    def calculate(self, s: str) -> int:
        stack = [ ]
        sign = 1
        num = 0

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)

            elif char == '(':
                stack.append(sign)
                stack.append('(')
                sign = 1
                
            elif char == '+':
                stack.append(sign * num)
                sign = 1
                num = 0
            elif char == '-':
                stack.append(sign * num)
                sign = -1
                num = 0
            elif char == ')':
                stack.append(num * sign)
                num = 0
                temp = 0
                while stack and stack[-1] != '(':
                    temp += stack.pop()
                stack.pop()
                sign = stack.pop()

                stack.append(sign * temp)
        
        if num != 0:
            stack.append(sign * num)
        return sum(stack)


            



        