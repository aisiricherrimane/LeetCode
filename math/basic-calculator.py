class Solution:
    def evaluate_expr(self, stack):
        # Compute the result of the expression in the stack
        res = 0
        sign = 1  # Tracks whether to add (+1) or subtract (-1)

        while stack:
            element = stack.pop()
            if isinstance(element, int):  # It's a number
                res += sign * element
            elif element == '+':
                sign = 1
            elif element == '-':
                sign = -1
        return res

    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        sign = 1  # Current sign for numbers (+1 or -1)

        for ch in s:
            if ch.isdigit():
                # Form the number
                operand = operand * 10 + int(ch)
            elif ch == '+':
                # Push the current operand and reset
                stack.append(sign * operand)
                operand = 0
                sign = 1
            elif ch == '-':
                # Push the current operand and reset
                stack.append(sign * operand)
                operand = 0
                sign = -1
            elif ch == '(':
                # Push the current result and sign onto the stack for later
                stack.append(sign)
                stack.append('(')
                operand = 0
                sign = 1
            elif ch == ')':
                # Push the last number before processing the parentheses
                stack.append(sign * operand)
                operand = 0

                # Evaluate the expression inside the parentheses
                res = 0
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.pop()  # Remove the '('
                
                # Apply the saved sign before '('
                sign = stack.pop()
                stack.append(sign * res)
                operand = 0

        # Add the last operand
        if operand != 0:
            stack.append(sign * operand)

        # Evaluate the remaining stack
        return sum(stack)
