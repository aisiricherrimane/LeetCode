class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr_num = 0
        sign = 1

        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            
            elif char == '+':
                stack.append(sign*curr_num)
                curr_num = 0
                sign = 1
            
            elif char == '-':
                stack.append(sign * curr_num)
                curr_num = 0
                sign = -1
            
            elif char == '(':
                stack.append(sign)
                stack.append('(')
                sign = 1

            elif char == ')':
                stack.append(sign * curr_num)
                curr_num = 0
                
                temp = 0
                while stack[-1] != '(':
                    temp += stack.pop()
                stack.pop()
                sign = stack.pop()

                stack.append(sign * temp)
        
        if curr_num > 0:
            stack.append(curr_num * sign)
        
        return sum(stack)


        