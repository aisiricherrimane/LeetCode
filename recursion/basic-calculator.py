class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(stack):
            res = stack.pop() if stack else 0
            while stack and stack[-1] != "(":
                sign = stack.pop()
                if sign == "+":
                    res += stack.pop()
                elif sign == "-":
                    res -= stack.pop()
            return res
        
        stack = []
        num, sign = 0, "+"
        i = 0

        while i < len(s):
            char = s[i]
            
            if char.isdigit():
                num = num * 10 + int(char)  # Build the current number
            elif char in "+-":
                if sign == "+":
                    stack.append(num)  # Add the current number to the stack
                elif sign == "-":
                    stack.append(-num)  # Add the negative of the current number
                num = 0  # Reset the current number
                sign = char  # Update the sign
            elif char == "(":
                stack.append(sign)  # Save the current sign
                stack.append("(")  # Mark the start of a sub-expression
                sign = "+"  # Reset sign for the sub-expression
            elif char == ")":
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                num = evaluate(stack)  # Solve the sub-expression
                stack.pop()  # Remove the "(" from the stack
            i += 1
        
        # Add the last number
        if sign == "+":
            stack.append(num)
        elif sign == "-":
            stack.append(-num)

        return evaluate(stack)  # Evaluate whatever is left in the stack
