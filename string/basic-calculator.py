class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(stack):
            res = 0 if not stack else stack.pop()
            while stack and stack[-1] != '(':
                sign = stack.pop()
                if sign == '+':
                    res += stack.pop()
                elif sign == '-':
                    res -= stack.pop()
            return res
        
        stack = []
        num = 0
        sign = '+'
        i = 0

        while i < len(s):
            char = s[i]
            if char.isdigit():
                num = num*10 + int(char)
            elif char in '+-':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                num = 0
                sign = char
            elif char == '(':
                stack.append(sign)
                stack.append("(")
                sign = '+'
            elif char == ')':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                num = evaluate(stack)
                
            i += 1
        
        if sign == '+':
            stack.append(num)
        elif sign == '-':
            stack.append(-num)
        
        return evaluate(stack)




                    
        