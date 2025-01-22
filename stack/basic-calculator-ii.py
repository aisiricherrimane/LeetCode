class Solution:
    def calculate(self, s: str) -> int:
        res = curr = prev = 0
        sign = '+'

        i = 0

        while i < len(s):
            char = s[i]

            if char.isdigit():
                curr = 0
                while i < len(s) and s[i].isdigit():
                    curr = curr* 10 + int(s[i])
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
                else:
                    res -= prev
                    res += int(prev / curr)
                    prev = int(prev / curr)

                curr = 0
            elif char != " ":
                sign = char
            i += 1
        return res
        