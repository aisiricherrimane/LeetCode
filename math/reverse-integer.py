class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = x * -1
        
        curr = 0

        while x > 0:
            last = x % 10
            curr = curr * 10 + last
            x = x // 10
        
        return curr * sign if (curr > -2**31 and curr < 2**31 - 1) else 0