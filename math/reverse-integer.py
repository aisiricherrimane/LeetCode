class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = -1 * x

        temp = 0

        while x > 0:
            digit = x % 10
            x = x // 10

            temp = temp * 10 + digit
        return temp * sign if (temp > -2**31 and temp < 2**31 - 1) else 0

        
       