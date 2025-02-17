class Solution:
    def calculate(self, s: str) -> int:
        
        res = curr = prev = 0
        sign = '+'
        i = 0

        while i < len(s):

            if s[i].isdigit():
                curr = 0
                while i < len(s) and s[i].isdigit():
                    curr = curr * 10 + int(s[i])
                    i += 1
                i -= 1
                if sign == '+':
                    res += curr
                    prev = curr
                elif sign == '-':
                    res -= curr
                    prev = -curr
                elif sign == '*':
                    res -= prev
                    res += prev * curr
                    prev = prev * curr
                elif sign == '/':
                    res -= prev
                    res += prev // curr
                    prev = prev // curr
                curr = 0
            elif s[i] != ' ':
                sign = s[i]
            i += 1
        return res

            
        