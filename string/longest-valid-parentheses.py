class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = 0
        right = 0
        maxlength = 0

        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            
            if left == right:
                maxlength = max(maxlength, 2 * right)
            elif right > left:
                left = right = 0
        
        left = right = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')':
                right += 1
            else:
                left += 1
            
            if left == right:
                maxlength = max(maxlength, 2 * right)
            elif left > right:
                left = right = 0
        
        return maxlength



















    
    def valid(self, s):
        stack = []
        for p in s:
            if p == ')':
                if stack and stack[-1] == ')':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return True if not stack else False
        